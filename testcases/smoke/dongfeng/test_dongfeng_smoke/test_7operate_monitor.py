
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
from time import sleep as sp


user = UserActivity()

mylogs = GetLogs()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        mylogs.log_info('-----------------------test_7operate_monitor---------------------------')
        
        # print('Wait for extract package finished', now_time)
        # sleep(10)
        mylogs.log_info('Start to execute test set env and launch ota at {}'.format(now_time))

    # @pytest.mark.skip(reson="skip this case")
    # def test_operate_monitor(self):
    #     """
    #     Usage: Set linux os envrionment before launching udsserver and esyncclient.
    #         : launch udsserver
    #     """
    #     try:
    #         launch_uds_status = CmdHelper.launch_terminal('udsserver','launch_udsserver_terminal.sh')
    #         sleep(5)
    #         launch_esync_status = CmdHelper.launch_terminal('esyncclient','launch_esyncclient_terminal.sh')
    #         sleep(5)
    #         launch_monitor_status = CmdHelper.launch_terminal('otamonitor','launch_otamonitor_terminal.sh')

    #         # assert launch_uds_status
    #     except Exception as msg:
    #         raise msg

    # sleep(2)

    # def test_launch_esync_client(self):
    #     """
    #     Usage: set linux os envrionment before launching udsserver and esuncclient.
    #         : launch esync client
    #     """
    #     # sleep(5)
    #     try:
    #         launch_esync_status = CmdHelper.launch_terminal('esyncclient','launch_esyncclient_terminal.sh')
    #         assert launch_esync_status
    #     except Exception as msg:
    #         raise msg

    # sleep(5)

    # def test_launch_otamonitor(self):
    #     """
    #     Usage: set linux os envrionment before launching udsserver and esyncclient.
    #         : launch otamonitor
    #     """
    #     sleep(5)
    #     try:
    #         launch_monitor_status = CmdHelper.launch_terminal('otamonitor','launch_otamonitor_terminal.sh')
    #         assert launch_monitor_status
    #     except Exception as msg:
    #         raise msg


    def test_operate_monitor(self):
        """
        Todo://1.connet,download,install
            2.take screen shot
        """
             
        user.click_connect_btn()
        sp(2)
        user.click_download_and_install_btn()
        sp(30)
        user.take_screen_shot()
        sp(1)
        user.click_close_btn()


    def teardown_class(self):
        """
        Execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # mylogs.log_info('-------------------------------------')
        mylogs.log_info('Finished to test launch ota at {}'.format(now_time))
        mylogs.log_info('test to execute close all terminals case')
        user.close_all_terminals()


if __name__ == "__main__":

    try:
        pytest.main(["test_7operate_monitor.py", "-s", '--html=test_7operate_monitor.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
