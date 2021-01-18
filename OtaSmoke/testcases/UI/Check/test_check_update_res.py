
"""
This module will execute all test cases for ota smoke automation.
Framework: pytest (version:6.2.1)
Python : 3.7.1
IDE: Pycharm 202.8194
"""

import sys
sys.path.append('/home/autotest/Downloads/OtaSmoke/common')
import pytest
from common_helper import *
from cmd_helper import *
from activity_helper import *
import datetime
# import allure

user = UserActivity()



# @allure.feature("OTA SMOKE AUTO TEST")
class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        execute one time before run all cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('start to execute smoke auto test', cur_time)

        path = judge_path()
        assert path

    def test_check_update_res(self):
        """
        Usage: To verify the result after execute download and update command.
        Success Value: 90 or 100
        """
        try:
            update_res = check_update_res()
            assert update_res
        except Exception as msg:
            raise msg

    def teardown_class(self):
        """
        execute one time after run all pytest cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('ota smoke auto test ending', cur_time)
        operate_ota = user.close_ota_monitor()



if __name__ == "__main__":

    try:
        pytest.main(["test_check_update_res.py", "-s", '--html=test_check_update_res.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
