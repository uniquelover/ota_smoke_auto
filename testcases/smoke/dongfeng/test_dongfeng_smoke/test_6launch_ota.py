
"""
@ --------------------------------------------------------------
This module will execute all test cases for ota smoke automation.
@ Framework: pytest (version:6.2.1)
@ Python : 3.7.1
@ IDE: Pycharm 202.8194
@ pytest-4.6.11
@ --------------------------------------------------------------
"""


import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
from logs import GetLogs
import pytest
from cmd_helper import *
from activity_helper import *
import datetime
from time import sleep


user = UserActivity()

mylogs = GetLogs()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before running all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('--------------------test_6launch_ota-----------------------------------')
        
        mylogs.log_info('Start to execute test set env and launch ota at {}'.format(now_time))

    # @pytest.mark.skip(reson="skip this case")
    def test_launch_ota(self):
        """
        Usage: Set linux os envrionment before launching udsserver and esyncclient
             : launch udsserver
        """
        try:
            CmdHelper.launch_terminal('setupdmtree','run_set_dmtree_script.sh')
            sleep(5)
            CmdHelper.launch_terminal('udsserver','launch_udsserver_terminal.sh')
            sleep(5)
            CmdHelper.launch_terminal('esyncclient','launch_esyncclient_terminal.sh')
            sleep(5)
            CmdHelper.launch_terminal('otamonitor','launch_otamonitor_terminal.sh')

        except Exception as msg:
            mylogs.log_error('Error occurs while launching ota due to {}'.format(msg))
            raise msg

    def teardown_class(self):
        """
        Execute one time after running all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('Finished to test launch ota at {}'.format(now_time))


if __name__ == "__main__":

    try:
        pytest.main(["test_6launch_ota.py", "-s", '--html=test_6launch_ota.html'])
    except Exception as e:
        raise e
