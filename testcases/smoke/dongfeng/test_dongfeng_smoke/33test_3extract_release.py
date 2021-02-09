
"""
@ --------------------------------------------------------------
This module will execute all test cases for ota smoke automation.
Framework: pytest (version:6.2.1)
Python : 3.7.1
IDE: Pycharm 202.8194
@ --------------------------------------------------------------
"""

import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
from logs import GetLogs
import pytest
from common_helper import *
import datetime

mylogs = GetLogs()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('--------------------test_3extract_release-----------------------------------')
        
        mylogs.log_info('Start to execute extract release at {}'.format(now_time))

    def test_extract_release(self):
        """
        Usage: Extract release file at target folder.
        Default path : /home/tiankang/Downloads/Excelforepackage
        """
        try:
            extract_status = extract_package()
            assert extract_status
        except Exception as msg:
            mylogs.log_error('Error occurs while exucuting test launch ota due to {}'.format(msg))
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # print('------------------------------------')
        mylogs.log_info('Finished to test extract release at {}'.format(now_time))


if __name__ == "__main__":

    try:
        pytest.main(["test_3extract_release.py", "-s", '--html=test_3extract_release.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
