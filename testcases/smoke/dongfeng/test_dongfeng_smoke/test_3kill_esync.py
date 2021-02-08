
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
from cmd_helper import *
import datetime

mylogs = GetLogs()


class TestOtaSmokeClass(object):


    def setup_class(self):
        """ 
        Execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('---------------------test_3kill_esync-----------------------------------')
        mylogs.log_info('Start to kill all esync before run ota smoke test at {}'.format(now_time))

    def test_kill_esync(self):
        """
        Kill all esync client before running ota smoke test
        """

        try:
            CmdHelper.kill_esync()
            # print(kill_esync_res)
            # assert kill_esync_res == "esyncclient: no process found"
        except Exception as msg:
            mylogs.log_error('Error occurs while killing all esync due to {}'.format(msg))
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('----------------------------------------')
        print('Kill all esync', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_3kill_esync.py", "-s", '--html=kill_esync_test.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
