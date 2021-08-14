from platform import system
import subprocess
import os
from icecream import ic
from pathlib import Path
from eliot import start_action, to_file

to_file(open("exec.log", "w"))
BINPATH = [str(Path.home()) + '/.local/bin']


def do_preChecks_navi():
    try:
        with start_action(action_type="preChecks_navi",
                          TARGET_OS=system().lower()):

            if system().lower() == 'linux':
                # Check if `~/.local/bin` is present, create otherwise
                with start_action(action_type='checkDir',
                                  DIR_NAME=BINPATH[0]):
                    if os.path.isdir(BINPATH[0]):
                        pass
                    else:
                        try:
                            with start_action(action_type='createDir'):
                                cmd = subprocess.run(['md', '-p', BINPATH[0]])
                                if cmd.returncode == 0:
                                    ic('[+] "~/.local/bin/" directory created'
                                       )
                                    pass
                                else:
                                    ic('[-]Failed to create directory')
                        except Exception as e:
                            raise str(e)

                # Deal with $PATH environment variable
                with start_action(action_type='checkEnvironVar',
                                  USER_HOME=str(Path.home())):
                    if str(Path.home()) + '/.local/bin' in os.environ['PATH']:
                        pass
                    else:
                        try:
                            with start_action(action_type='appendToPATH',
                                              USER_HOME=str(Path.home())):
                                os.environ['PATH'] = os.pathsep.join(
                                    [BINPATH[0], os.environ['PATH']])
                        except Exception as e:
                            raise str(e)
            elif system().lower() == 'darwin':
                ic('Do Mac OS X stuff here')
            else:
                pass
    except Exception as e:
        raise str(e)


if __name__ == "__main__":
    do_preChecks_navi()
