#!/usr/bin/env python3

"""
This module submit a basic class to launch test script by kinds of config file
and an unique entrance for total test framework.

@ module name: execute
@ date: 12/14/2020

"""

import parser
import os
import time
import pytest

SETUP_STAGE = 0
MAIN_STAGE = 1
TEARDOWN_STAGE = 1


class Configration:

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
    pass


def main(config, skip_setup=False, skip_main_step=False):
    pass