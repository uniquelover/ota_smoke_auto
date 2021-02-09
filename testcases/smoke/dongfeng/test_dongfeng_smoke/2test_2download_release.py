
"""
@ --------------------------------------------------------------
This module will execute all test cases for ota smoke automation.
@ Framework: pytest (version:6.2.1)
@ Python : 3.7.1
@ IDE: Pycharm 202.8194
@ --------------------------------------------------------------
"""

import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
import pytest
from common_helper import *
import datetime



class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('Start to execute smoke auto test', now_time)
        sleep(10)

    def test_download_release(self):
        """
        Usage: Download latest release form the url given by dev
        """
        try:
            down_status = download_release()
            assert down_status
        except Exception as msg:
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('test download latest release ending', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_2download.py", "-s", '--html=ota_download_test.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
