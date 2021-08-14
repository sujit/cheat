from platform import system
import subprocess
from os import environ, path
from icecream import ic
from pathlib import Path
from eliot import start_action, to_file

to_file(open("exec.log", "w"))


def do_getPlatform():
    PATHLIST = [str(Path.home()) + '/.local/bin']

    try:
        with start_action(action_type="getPlatform",
                          target_os=system().lower()):
            if system().lower() == 'linux':

                # Check if `~/.local/bin` is present, create otherwise
                with start_action(action_type='checkDir',
                                  target_dir=PATHLIST[0]):
                    if path.isdir(PATHLIST[0]):
                        pass
                    else:
                        try:
                            with start_action(action_type='createDir'):
                                cmd = subprocess.run(['md', '-p', PATHLIST[0]])
                                if cmd.returncode == 0:
                                    ic('[+] Create: "~/.local/bin/" successful')
                                    pass
                                else:
                                    ic('[-]Failed to create directory')
                        except Exception as e:
                            raise str(e)

                # Deal with $PATH environment variable
                with start_action(action_type='checkEnvironVar',
                                  basePath=str(Path.home())):
                    if str(Path.home()) + '/.local/bin' in environ['PATH']:
                        pass
                    else:
                        print('bummer.. we need to feed path to $PATH')
            elif system().lower() == 'darwin':
                ic('Do Mac OS X stuff here')
            else:
                pass
    except Exception as e:
        raise str(e)


def task_print_echo_to_stdout():
    """Pre-checks followed-by tool install"""
    return {
        'actions': [do_getPlatform],
        'verbosity': 2
    }
