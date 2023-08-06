import re
import functools
import json
import subprocess
import inspect
import logging
import pathlib
import tempfile
import datetime
import os
import copy
import math
from string import Template
from importlib import resources

import hyclib as lib

from . import config, utils

logger = logging.getLogger(__name__)
run_script = resources.files('slurm_parallel').joinpath('run.sh')
run_py_script = resources.files('slurm_parallel').joinpath('run.py')
cleanup_script = resources.files('slurm_parallel').joinpath('cleanup.sh')

allowed_args = {'A', 'account', 'acctg_freq', 'batch', 'bb', 'bbf', 'b', 'begin', 'D', 'chdir', 'cluster_constraint', 'M', 'clusters', 'comment', 'C', 'constraint', 'container', 'container_id', 'contiguous', 'S', 'core-spec', 'cores_per_socket', 'cpu_freq', 'cpus_per_gpu', 'c', 'cpus_per_task', 'deadline', 'delay_boot', 'd', 'dependency', 'm', 'distribution', 'e', 'error', 'x', 'exclude', 'exclusive', 'export', 'export_file', 'extra', 'B', 'extra_node_info', 'get_user_env', 'gid', 'gpu_bind', 'gpu_freq', 'G', 'gpus', 'gpus_per_node', 'gpus_per_socket', 'gpus_per_task', 'gres', 'gres_flags', 'h', 'help', 'hint', 'H', 'hold', 'ignore_pbs', 'i', 'input', 'J', 'job_name', 'kill_on_invalid_dep', 'L', 'licenses', 'mail_type', 'mail_user', 'mcs_label', 'mem', 'mem_bind', 'mem_per_cpu', 'mem_per_gpu', 'mincpus', 'network', 'nice', 'k', 'no_kill', 'no_requeue', 'F', 'nodefile', 'w', 'nodelist', 'N', 'nodes', 'n', 'ntasks', 'ntasks_per_core', 'ntasks_per_gpu', 'ntasks_per_node', 'ntasks_per_socket', 'open_mode', 'O', 'overcommit', 's', 'oversubscribe', 'p', 'partition', 'power', 'prefer', 'priority', 'profile', 'propagate', 'q', 'qos', 'Q', 'quiet', 'reboot', 'requeue', 'reservation', 'signal', 'sockets_per_node', 'spread_job', 'switches', 'test_only', 'thread_spec', 'threads_per_core', 't', 'time', 'time_min', 'tmp', 'tres_per_task', 'uid', 'usage', 'use_min_nodes', 'v', 'verbose', 'V', 'version', 'W', 'wait', 'wait_all_nodes', 'wckey', 'wrap'}

__all__ = ['parallelize']

class StringTemplate(Template):
    delimiter = '%'
    idpattern = "(?a-i:[sF])" # ASCII-only, don't ignore case

@lib.functools.parametrized
def parallelize(func, database=None, table=None, columns=None, max_n_tasks=None, tmp_dir=None, out_dir=None, out_file=None, time_per_config=30, **default_kwargs):
    for k in default_kwargs:
        if k not in allowed_args:
            raise KeyError(f"parallelize got an unexpected argument '{k}'")
            
    funcname = func.__name__
    filename = inspect.getsourcefile(func)
    
    if table is None:
        table = funcname

    def run_task(tmp_file):
        n_tasks = int(os.environ['SLURM_ARRAY_TASK_COUNT'])
        task_id = int(os.environ['SLURM_ARRAY_TASK_ID'])
        
        logger.info(f"Running task {task_id}...")
        
        with open(tmp_file, 'r') as f:
            configs = json.load(f)
            
        config_indices = range(task_id, len(configs), n_tasks)
        
        logger.info(f"Config indices: {config_indices}")

        for i in config_indices:
            config = configs[i]
            
            result = func(**config)

            logger.info(f"Finished config {i}.")

            if database is not None:
                if table not in database:
                    raise RuntimeError(f"{table=} not found in {database=}.")
                    
                if columns is not None:
                    if isinstance(columns, str):
                        result = {columns: result}
                    else:
                        result = {column: v for v in result}

                database[table].append(config | result)

                logger.info(f"Saved output of config {i}.")
    
    def remote(configs, max_n_tasks=max_n_tasks, tmp_dir=tmp_dir, out_dir=out_dir, out_file=out_file, time_per_config=time_per_config, **kwargs):
        for k in kwargs:
            if k not in allowed_args:
                raise KeyError(f"remote got an unexpected argument '{k}'")
                
        if max_n_tasks is None:
            completed_process = subprocess.run(
                ['scontrol', 'show', 'config'],
                capture_output=True,
                check=True,
            )
            max_n_tasks = int(re.search('MaxArraySize\s*= (\d*)', completed_process.stdout.decode("utf-8")).group(1))
                
        if tmp_dir is None and 'tmp_dir' in config:
            tmp_dir = config['tmp_dir']

        if out_dir is None:
            out_dir = config['out_dir']

        if out_file is None:
            out_file = config['out_file']
            
        if not isinstance(time_per_config, datetime.timedelta):
            time_per_config = datetime.timedelta(minutes=time_per_config)
            
        pathlib.Path(tmp_dir).mkdir(parents=True, exist_ok=True)
        out_dir = StringTemplate(out_dir).safe_substitute(s=pathlib.Path(filename).stem, F=funcname)
        out_dir = pathlib.Path(datetime.datetime.now().strftime(out_dir))
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = StringTemplate(out_file).safe_substitute(s=pathlib.Path(filename).stem, F=funcname)
        
        n_configs = len(configs)
        n_tasks = min(n_configs, max_n_tasks)
        time_per_task = int(math.ceil(n_configs / n_tasks)) * time_per_config
        
        run_kwargs = {
            'c': 2,
            'mem_per_cpu': '2gb',
            'time': lib.datetime.strftime(time_per_task, '%d-%H:%M:%S'),
            'array': f'0-{n_tasks-1}',
            'output': out_dir / out_file,
            'parsable': True,
            'job_name': f'{pathlib.Path(filename).stem}_{funcname}',
        } | default_kwargs | kwargs
        run_options = utils.to_cmd_options(**run_kwargs)
        
        try:
            with tempfile.NamedTemporaryFile(dir=tmp_dir, mode='w', delete=False) as f:
                json.dump(configs, f)
                
            tmp_file = pathlib.Path(f.name)
            logger.info(f"Saved configs to tmp file {tmp_file}.")
            
            completed_process = subprocess.run(
                ["sbatch", *run_options, str(run_script), str(run_py_script), filename, funcname, str(tmp_file)],
                capture_output=True,
                check=True,
            )
        
            run_PID = completed_process.stdout.decode("utf-8").split('\n')[-2]

            logger.info(f"Submitted job to cluster to run {funcname} with job ID {run_PID}.")
            logger.debug(f"Submission command: {completed_process.args}")
            
            cleanup_kwargs = {
                'c': 1,
                'mem_per_cpu': '1mb',
                'time': 1, # 1 minute
                'dependency': f'afterany:{run_PID}',
                'output': out_dir / "cleanup.out",
                'parsable': True,
                'job_name': f'{pathlib.Path(filename).stem}_{funcname}_cleanup',
            }
            cleanup_options = utils.to_cmd_options(**cleanup_kwargs)

            completed_process = subprocess.run(
                ["sbatch", *cleanup_options, str(cleanup_script), str(tmp_file)],
                capture_output=True,
                check=True,
            )
            
        except Exception as err:
            tmp_file.unlink()
            raise err
        
        cleanup_PID = completed_process.stdout.decode("utf-8").split('\n')[-2]
        
        logger.info(f"Submitted job to cluster to run cleanup with command job ID {cleanup_PID}.")
        logger.debug(f"Submission command: {completed_process.args}")
        
        return run_PID
    
    func.run_task = run_task
    func.remote = remote
    
    return func
        
