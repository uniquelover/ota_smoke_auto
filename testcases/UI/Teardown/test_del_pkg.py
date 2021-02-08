
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
import allure



@allure.feature("OTA SMOKE AUTO TEST")
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

    @pytest.mark.skip(reson="skip this case")
    def test_download_release(self):
        """
        function: download latest release form url given by dev
        """
        try:
            status = download_release()
            assert status
        except Exception as msg:
            raise msg

    # def test_judge_path(self):
    #     """
    #     function: whether the folder exists to save release or not
    #     """
    #     path = judge_path()
    #     assert path

    @pytest.mark.skip(reson="skip second case")
    def test_extract_package(self):
        try:
            extract_res = extract_package()
            assert extract_res
        except Exception as msg:
            raise msg


    def test_check_env(self):
        try:
            env_status = check_env()
            assert env_status
        except Exception as msg:
            raise msg

    def test_check_update_res(self):
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


# if __name__ == "__main__":

#     try:
#         pytest.main(["test_ota_smoke.py", "-s", '--html=ota_smoke_test.html'])
#     except Exception as e:
#         raise e
#     finally:
#         print('ota smoke auto test completed')
