
from os.path import dirname
import subprocess
import sys


def run(run_fn, file_location):

    # construct the arguments to run coverage
    args = [sys.executable, '-m', 'coverage',
                            'run', '--source', dirname(file_location),
                            file_location, '--coverage-passthru'] + sys.argv[1:]
    
    retval = subprocess.call(args)
    if retval != 0:
        return retval
    
    args = [sys.executable, '-m', 'coverage',
                            'report', '-m']
    
    return subprocess.call(args)
    