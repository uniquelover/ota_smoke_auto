
"""
This module will execute all test cases for ota smoke automation.
@ Framework: pytest (version:6.2.1)
@ Python : 3.7.1
@ IDE: Pycharm 202.8194
"""

import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
from logs import GetLogs
import pytest
from common_helper import *
from file_helper import *
import datetime

mylogs = GetLogs()


class TestOtaSmokeClass(object):


    def setup_class(self):
        """ 
        Execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('--------------------test_1delete_fumo---------------------------------')
        mylogs.log_info('Start to delete fumo files before run ota smoke at {}'.format(now_time))

    def test_create_folder(self):
        fumo_path = '/home/tiankang/Downloads/data/dm_tree/FUMO'
        try:
            del_fumo_res = OtaFileOperate.delete_file_or_folder(fumo_path,"all")
            assert del_fumo_res
        except Exception as msg:
            mylogs.log_error('Error occurs while executing test delete fumo due to {}'.format(msg))
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('----------------------------------------')
        print('Create folder auto test ending', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_1delete_fumo.py", "-s", '--html=del_fumo_test.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
