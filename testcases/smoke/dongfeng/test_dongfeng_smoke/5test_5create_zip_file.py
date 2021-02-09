
"""
@ ----------------------------------------------------------------
@ This module will execute all test cases for ota smoke automation.
@ Framework: pytest (version:6.2.1)
@ Python : 3.7.1
@ IDE: Pycharm 202.8194
@ ----------------------------------------------------------------
"""

import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
from logs import GetLogs
import pytest
from common_helper import *
import datetime
from time import sleep


mylogs = GetLogs()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('--------------------test_5create_zip_file-----------------------------------')
        mylogs.log_info('Start to execute create zip and doip at {}'.format(now_time))

    def test_create_zip_file(self):
        """
        Usage: Create doip folder and update.zip before executing udsserver and esyncclient.
        """
        target_path = "/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/doip"
        try:
            create_zip_status = create_path(target_path,'update.zip',True)
            assert create_zip_status
        except Exception as msg:
            mylogs.log_error('Error occurs while exucuting test launch ota due to {}'.format(msg))
            raise msg



    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('Create doip folder and zip file successfully at {}'.format(now_time))


if __name__ == "__main__":

    try:
        pytest.main(["test_5create_zip_file.py", "-s", '--html=test_5create_zip_file.html'])
    except Exception as e:
        raise e