#!/usr/bin/env python3


"""
@ name: runcmd
@ date: 12/10/2020 16:13
@ function: execute cmd or shell commands on linux or windows
"""



import subprocess
import os


class RunCmd:

    def __init__(self):
        """
        @ init instance method
        """
        pass

    @staticmethod
    def run_cmd(cmd, platform='posix'):
        """
        @ params: cmd string
        @ return: subprocess object
        """
        os.system(cmd)
        # os.popen(cmd)
        # subprocess.Popen(cmd)
        if os.name == 'posix':
            print('linux platform')
        elif os.name == 'nt':
            print('windows platform')
        else:
            print('others platform')

        if platform == 'posix':
            print('linux')
        
        if platform == 'nt':
            print('windowsSSS')

    @staticmethod
    def __run_cmds(self, cmds, platform='posix', *args, **kwargs):
        """
        @ params:
        cmds: list 
        @ return:
        """

        print("input params is %s" % cmds)
        # pass

    def run_cmd_line(self, cmds):
        self.__run_cmds(cmds)
        print('only for test')


class RunShell(RunCmd):

    __cmd = 'python -m'
    
    def __init__(self, shell_cmd):
        self.shell_cmd = shell_cmd
        self.__shell_version = 1
        self._shell_date = 2

    def run_shell_cmd(self):
        print(self.shell_cmd)
        i = 2
        print('yes') if i > 1 else print('no')

    def get_shell_date(self):
        print(self._shell_date)


if __name__ == "__main__":
    run = RunCmd()
    # RunCmd.run_cmd('dir','nt')
    # RunCmd.run_cmd('dir')
    # run.run_cmd_line('dir')
    # run.__run_cmd('dir')
    # print(dir(run))


    # shellrun = RunShell('dir')

    # shellrun.get_shell_date()

    shellrun1 = RunShell('dir')

    print(shellrun1._RunShell__cmd)

    print(RunShell.__cmd)

    print(shellrun1._shell_date)

    shellrun1.run_shell_cmd()

    # shellrun.run_cmd('dir')
    
    # shellrun.__run_cmds('dir')

    # shellrun.__shell_version

