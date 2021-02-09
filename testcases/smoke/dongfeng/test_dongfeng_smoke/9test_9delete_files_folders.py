
"""
This module will execute all test cases for ota smoke automation.
@ Framework: pytest (version:6.2.1)
@ Python : 3.7.1
@ IDE: Pycharm 202.8194
"""

import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/common')
import pytest
from common_helper import *
from cmd_helper import *
from activity_helper import *
from file_helper import *
import datetime


user = UserActivity()



class TestOtaSmokeClass(object):

    def setup_class(self):
        """
        Execute one time before run all test cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------------')
        print('Start to delete campaigns and campaignState folders', cur_time)

        path = judge_path()
        assert path

    def test_delete_files_folders(self):
        """
        Usage: To verify the result after execute download and update command.
        
        """
        cam_path = '/home/tiankang/Downloads/dm_tree/DevInfo/Ext/Excelfore/Campaigns'
        cams_path = '/home/tiankang/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState'
        try:
            del_cam_res = OtaFileOperate.delete_file_or_folder(cam_path)
            del_cams_res = OtaFileOperate.delete_file_or_folder(cams_path)
            assert del_res,del_cams_res
        except Exception as msg:
            raise msg

    def teardown_class(self):
        """
        Execute one time after run all test cases
        """
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        print('------------------------------------')
        print('Delete campaigns and campaignState folder successfully', cur_time)
        operate_ota = user.close_ota_monitor()



if __name__ == "__main__":

    try:
        pytest.main(["test_check_update_res.py", "-s", '--html=test_check_update_res.html'])
    except Exception as e:
        raise e
    # finally:
    #     print('ota smoke auto test completed')
