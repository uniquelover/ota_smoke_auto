
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
from file_helper import *
import datetime
from time import sleep

mylogs = GetLogs()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('--------------------test_4check_extract_folder-----------------------------------')
        
        mylogs.log_info('Start to execute check extract release at {}'.format(now_time))

    def test_check_extract_release(self):
        """
        Usage: Create doip folder and update.zip before executing udsserver and esyncclient.
        """
        bin_path = '/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin'
        try:
            extract_result = OtaFileOperate.check_extract_package(bin_path)
            assert extract_result
        except Exception as msg:
            mylogs.log_error('Error occurs while exucuting test launch ota due to {}'.format(msg))
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # print('------------------------------------------')
        mylogs.log_info('Check extracted release successfully at {}'.format(now_time))


if __name__ == "__main__":

    try:
        pytest.main(["test_4check_extract_folder.py", "-s", '--html=test_4check_extract_folder.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
