
"""
This module will execute all test cases for ota smoke automation.
@ Framework: pytest (version:6.2.1)
@ Python : 3.7.1
@ IDE: Pycharm 202.8194
"""

import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
import pytest
from common_helper import *
from cmd_helper import *
from activity_helper import *
import datetime


user = UserActivity()



class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('-------------------------------------------')
        print('Start to test check ota update result', cur_time)

        path = judge_path()
        assert path

    def test_check_update_result(self):
        """
        Usage: To verify the result after executing ota download and update action.
        Success Value: 90 or 100
        """
        try:
            update_res = check_update_res_fumo()
            assert update_res
        except Exception as msg:
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('test check update result ending', cur_time)
        #operate_ota = user.close_ota_monitor()



if __name__ == "__main__":

    try:
        pytest.main(["test_8check_update_result.py", "-s", '--html=test_8check_update_res.html'])
    except Exception as e:
        raise e