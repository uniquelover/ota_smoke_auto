
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
from activity_helper import *
from file_helper import *
import datetime


user = UserActivity()

mylogs = GetLogs()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('------------------test_10collect_esync_log------------------------')
        mylogs.log_info('Start to collect esync log at {}'.format(cur_time))


    def test_collect_esync_log(self):
        """
        Usage: To collect esync client error log.
        
        """
        
        try:
            filter()
        except Exception as msg:
            mylogs.log_error('Error occurs while collectting esync log due to {}'.format(msg))
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # mylogs.log_info('------------------------------------')
        mylogs.log_info('Collect esync log successfully at {}'.format(cur_time))
        # operate_ota = user.close_ota_monitor()



if __name__ == "__main__":

    try:
        pytest.main(["test_10collect_esync_log.py", "-s", '--html=test_10collect_esync_log.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')