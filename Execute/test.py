#!/usr/bin/env python3

"""
@ ----------------------------------------------------------------------------
This module submit a basic class to launch test script by kinds of config file
and an unique entrance for total test framework.

@ Module name: execute
@ Create on: 12/14/2020
@ Author: tiankang <kang.tian@excelfore-china.com>
@ Version: v1.0dongfeng
@ ----------------------------------------------------------------------------
"""


import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/testframework/run_test')
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
from runtests import *
from cmd_helper import *
import argparse
import os
import time
import subprocess


SETUP_STAGE = 0
MAIN_STAGE = 1
TEARDOWN_STAGE = 1


class Configuration:

    """
    A class for execute python script by command line and config file.
    """

    def __init__(self):

        self.execution.max_times = None
        self.execution.min_times = None
        self.execution.main_list = ''
        self.loop.folder_prefix = 'loop'
        self.loops = 1
        self.settings = []

    def load_config_file(self, filepath):
        temp_setting_dict = {}
        if not os.path.isfile(filepath):
            raise IOError("{0} is not a file".format(filepath))
        exec(filepath, {}, temp_setting_dict)
        for key in temp_setting_dict.keys():
            setattr(self, key, temp_setting_dict[key])


def command_format():
    pass


def execute_cmd(cmd):
    print ("Executing command " + cmd)
    try:

        os.system(cmd)

    except Exception as e:

        print ('Execution command exception: ' + str(e))
        return

def ask_if_continue():
    """Asks the user if they want to continue execution.

    Returns:
        True of False if the user wishes to continue.
    """
    answer = None
    acceptable_answers = ['yes', 'no', 'y', 'n']
    while answer not in acceptable_answers:
        answer = input('Do you wish to continue executing the script((y)es/(n)o)?')
    return answer in ['yes', 'y']


# def main():

    # arg = get_url()

    # print(type(arg))

    # print(arg)

    # print('host=', parser.server)
    # exit_code = 0

def get_url():

    parser = argparse.ArgumentParser(description="This is description")

    parser.add_argument('configuration_file', type=str,
                        help='A path to a configuration file.')

    parser.add_argument('--host', action='store',
                        dest='server',default="localhost", help='connect to host')


    return parser.parse_args()


# def run_main():

#     CmdHelper.launch_terminal('main','launch_main.sh')
    



if __name__ == "__main__":
    # get_url()
    # main()
    # execute_cmd('pytest ../testcases/smoke/test_ota_smoke.py')
    # parser = argparse.ArgumentParser()
    # parser.add_argument('configuration_file', type=str,
    #                     help='A path to a configuration file.')
    # args = parser.parse_args()
    # config_file = args.configuration_file
    # configuration = Configuration()
    # configuration.load(config_file)

    # execfile('/home/tiankang/Downloads/OtaSmoke/testframework/run_test/runtests.py')
    main('/home/tiankang/Downloads/OtaSmoke/testcases/smoke/dongfeng/test_dongfeng_smoke','--html=/home/tiankang/Downloads/OtaSmoke/Logs/dongfeng/test_dongfeng_ota_smoke.html')
    # run_main()
