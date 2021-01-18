
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
import datetime
# import allure



# @allure.feature("OTA SMOKE AUTO TEST")
class TestOtaSmokeClass(object):


    def setup_class(self):
        """
        execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('start to execute create folser method test', now_time)

    def test_check_env(self):
        try:
            extract_folder_status = create_path()
            assert extract_folder_status
        except Exception as msg:
            raise msg

    def teardown_class(self):
        """
        execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('create folder auto test ending', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_create_folder.py", "-s", '--html=ota_smoke_test.html'])
    except Exception as e:
        raise e
    finally:
        print('ota smoke auto test completed')
