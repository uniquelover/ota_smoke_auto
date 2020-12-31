#!/usr/bin/ env python3

"""
name: test.py
functions: test configparser moudle
time: 17:34
ide: vs code
"""

import os
import configparser
import celery
import pytest

print ('test')


def generate_cmd(Project_Name, CI_IP,Project_Code_File, Project_Exclude_File, Project_Backup_Dir, Project_Deploy_Path,
                 Project_Start_Command, Project_Log_Path):
    # cmd = []
    pass


def __generate_cmd():

    cmd = []

    cmd.append("mkvirtualenv myenv")

    cmd.append("python test.py")

    return cmd


def test_generate_cmd():
    ccmd = __generate_cmd()
    if ccmd:
        print("yes")
        print(ccmd)
        for i in ccmd:
            print(i)


def test_one():
    print('test_one founction-----')
    assert 1


if __name__ == "__main__":
    # test_generate_cmd()
    pytest.main('-s test.py')