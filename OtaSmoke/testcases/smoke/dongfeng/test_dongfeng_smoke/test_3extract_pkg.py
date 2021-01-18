
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



class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('Start to execute smoke auto test', now_time)

    def test_download_release(self):
        """
        Usage: Extract release file at target folder.
        Default path : /home/autotest/Downloads/Excelforepackage
        """
        try:
            extract_status = extract_package()
            assert extract_status
        except Exception as msg:
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('Test extract pkg file ending', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_extract_pkg.py", "-s", '--html=test_extract_pkg.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
