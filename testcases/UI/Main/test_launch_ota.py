
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
from cmd_helper import *
from activity_helper import *
import datetime
from time import sleep


user = UserActivity()


class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        execute one time before run all cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('start to execute test set  env and launch ota', now_time)

    # @pytest.mark.skip(reson="skip this case")
    def test_launch_udsserver(self):
        """
        Usage: set linux os envrionment before launching udsserver and esuncclient.
            : launch udsserver
        """
        try:
            launch_uds_status = CmdHelper.launch_terminal('udsserver','launch_udsserver_terminal.sh')
            assert launch_uds_status
        except Exception as msg:
            raise msg

    # @pytest.mark.skip(reson="skip this case")
    def test_launch_esync_client(self):
        """
        Usage: set linux os envrionment before launching udsserver and esuncclient.
            : launch esync client
        """
        sleep(5)
        try:
            launch_esync_status = CmdHelper.launch_terminal('esyncclient','launch_esyncclient_terminal.sh')
            assert launch_esync_status
        except Exception as msg:
            raise msg


    def test_launch_otamonitor(self):
        """
        Usage: set linux os envrionment before launching udsserver and esyncclient.
            : launch otamonitor
        """
        sleep(5)
        try:
            launch_monitor_status = CmdHelper.launch_terminal('otamonitor','launch_otamonitor_terminal.sh')
            assert launch_monitor_status
        except Exception as msg:
            raise msg


    def test_operate_otamonitor(self):
             
        # user = UserActivity()

        operate_ota = user.operate_ota_monitor()


    # sleep(5)

    # def test_close_otamonitor(self):

    #     operate_ota = user.close_ota_monitor()


    def teardown_class(self):
        """
        execute one time after run all pytest cases
        """
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('test launch ota ending', now_time)


if __name__ == "__main__":

    try:
        pytest.main(["test_launch_ota.py", "-s", '--html=test_launch_ota.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
