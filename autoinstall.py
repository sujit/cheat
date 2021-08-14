from platform import system
import subprocess
import os
import glob
from icecream import ic
from pathlib import Path, PurePath
import shutil
from eliot import start_action, to_file

to_file(open("exec.log", "w"))

BINPATH = [str(Path.home()) + '/.local/bin']
CHEATS_FILE_NAVI = 'cheats/tool.navi/'
CHEATS_FILE_CHEAT = 'cheats/tool.cheat/'


def do_preInstallChecks():
    try:
        with start_action(action_type="preChecks",
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
                                cmd = subprocess.run(['mkdir', '-p', BINPATH[0]])
                                if cmd.returncode == 0:
                                    print('[+] "~/.local/bin/" directory created')
                                else:
                                    print('[-]Failed to create directory')
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
                print('[+]MacOS stuff goes here')
            else:
                pass
    except Exception as e:
        raise str(e)


def do_install_navi():
    try:
        print('[*]navi install check in-progress')
        with start_action(action_type='init_install_navi'):
            if system().lower() == 'linux' and (os.path.isfile(BINPATH[0] +
                '/' + 'navi') and os.path.isfile(BINPATH[0] + '/' + 'fzf')):
                print('[i]navi pre-installed. No actions taken.')
            else:
                binaries = ['bins/fzf.lin', 'bins/navi.lin']
                for index in binaries:
                    bin_name = PurePath(index)
                    with start_action(action_type='copy_bin',
                                      SOURCE_BINARY=bin_name.stem,
                                      COPY_TARGET_PATH=BINPATH[0]):
                        cmd = subprocess.run(['cp', index, BINPATH[0] + '/' + bin_name.stem])
                        if cmd.returncode == 0:
                            print('[+]%s copied to %s' % (bin_name.stem, BINPATH[0]))
                        else:
                            print('[-]binary copy failed')
    except Exception as e:
        raise str(e)

    try:
        with start_action(action_type='init_create_navi_cheats_dir'):
            if system().lower() == 'linux':
                navi_cheats = str(Path.home()) + '/.local/share/navi/cheats/awake__cheats'
                cmd2 = subprocess.run(['mkdir', '-p', navi_cheats])
                if cmd2.returncode == 0:
                    print('[i]navi cheats path: %s' % (navi_cheats))
                    with start_action(action_type='copy_cheats', recursive=True):
                        for index in glob.iglob('cheats/tool.navi/*', recursive=True):
                            shutil.copy(index, navi_cheats)
                else:
                    print('[-]Failed to create directory')
            elif system().lower() == 'darwin':
                print('Mac stuff goes here..')
    except Exception as e:
        raise str(e)


if __name__ == "__main__":
    do_preInstallChecks()
    do_install_navi()
