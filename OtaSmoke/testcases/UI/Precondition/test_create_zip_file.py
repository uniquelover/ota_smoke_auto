
"""
@ --------------------------------------------------------------
This module will execute all test cases for ota smoke automation.
Framework: pytest (version:6.2.1)
Python : 3.7.1
IDE: Pycharm 202.8194
@ --------------------------------------------------------------
"""

import sys
sys.path.append('/home/autotest/Downloads/OtaSmoke/common')
import pytest
from common_helper import *
import datetime
from time import sleep


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('start to execute test env and launch terminal', now_time)

    def test_launch_udsserver(self):
        """
        Usage: create doip folder and update.zip before executing udsserver and esyncclient.
        """
        target_path = "/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin/doip"
        try:
            create_zip_status = create_path(target_path,'update.zip',True)
            assert create_zip_status
        except Exception as msg:
            raise msg



    def teardown_class(self):
        """
        execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('test set env ending', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_create_zip_file.py", "-s", '--html=test_create_zip_file.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
