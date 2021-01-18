
"""
@ ------------------------------------------------
@ Name: cmd_helper.py
@ Usage: execute shell cmd under ubuntu
@ Created on: 1/7/2021
@ Author: tiankang <kang.tian@excelfore-china.com>
@ ------------------------------------------------
"""

import sys
sys.path.append('/home/autotest/Downloads/OtaSmoke/Mylog')
import requests
import os
from time import sleep
from logs import GetLogs
import subprocess






class CmdHelper:
    
    def __init__(self):

        pass


    @staticmethod
    def launch_terminal(terminal_name,script_path):

        cmd = "gnome-terminal --full-screen -t {0} -e 'bash -c \"source ./{1}; exec bash\"'".format(terminal_name,script_path)

        # print(cmd) 

        if os.path.exists(script_path):

            try:

                # os.system(cmd)

                # os.popen(cmd)

                subprocess.Popen(cmd,stdin=subprocess.PIPE, shell=True, bufsize=4096)

                return True

            except Exception as e:
            	print('Error happen while executing cmd due to {}'.format(e))
            	raise e


    @staticmethod
    def run_cmd(self,cmd, cwd=None, timeout=None, shell=False):
        """
        param: cmd, the command will be executed
        param: cwd, the work direction where command executed
        param: timeout, set time when executing command
        param: shell, will use linux shell mode if set True
        """
        import subprocess
        import shlex
        mylogs.log_info('Executing command:' + ' ' + cmd)
        try:
            if shell:
                ccmd = cmd
            else:
                ccmd = shlex.split(cmd)
            proc = subprocess.Popen(ccmd, shell=shell)
            proc.wait()
            if proc.returncode != 0:
                raise Exception('Execute command return value was not 0!')
        except Exception as e:
            mylogs.log_info('---------FAILURE MESSAGE-------')
            mylogs.log_info('Error message is %s' % e)
            mylogs.log_info('---------FAILURE MESSAGE-------')


    @staticmethod
    def run_cmds(cmd, cwd=None, timeout=None, shell=False):

        if shell:
            ccmd = cmd
        else:
            ccmd = shlex.split(cmd)

        print('execute command {}'.format(ccmd))
        sleep(3)
        end_time = 0
        if timeout:

            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

        if cwd:
            print('command run in {}'.format(cwd))
        else:
            print('-------no cwd---------')

        sub = subprocess.Popen(ccmd, cwd=cwd, stdin=subprocess.PIPE, shell=shell, bufsize=4096)

        while sub.poll() is None:
            sleep(0.5)
            if timeout:
                if end_time <= datetime.datetime.now():
                    raise Exception('Timeout {}'.format(ccmd))
        return str(sub.returncode)


if __name__ == "__main__":

    CmdHelper.launch_terminal('udsserver','launch_udsserver_terminal.sh')
    # sleep(5)

    # CmdHelper.launch_terminal('esyncclient','launch_esyncclient_terminal.sh')
    # sleep(5)

    # CmdHelper.launch_terminal('otamonitor','launch_otamonitor_terminal.sh')