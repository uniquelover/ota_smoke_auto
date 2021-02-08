"""
@ ------------------------------------------------------------------------------
module to simulate some user activities with ota monitor both mouse and keyboard.

@ Created on: 1/6/2021
@ Author: tiankang <kang.tian@excelfore-china.com>
@ Lience: <your lience>
@ -------------------------------------------------------------------------------
"""

try:
    from pymouse import PyMouse
    from pykeyboard import PyKeyboard
except:
    pass

import time
from functools import wraps
import inspect
from time import sleep		 
import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
from logs import GetLogs
import os

mylogs = GetLogs()


def get_func_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        mylogs.log_info('Now executing is %s' % func.__name__)
        return r
    return wrapper



class UserActivity:
    
    k = PyKeyboard()

    def __init__(self):

        """
        Call pymouse and pykeyboard method
        Set default click event times 1
        Set default Interval time bewteen two times 0
        """

        self.m = PyMouse()
        self.k = PyKeyboard()
        self.click_times = 1
        self.sleep_times = 0


    @get_func_name
    def click_tab_key(self,sleep_times,run_times=0,*args):
        try:
            if run_times:

                run = run_times

            else:
                run = self.click_times

            mylogs.log_info('clicking tab key will be executed %d times' % run)

            for _ in range(0,run):
                if sleep_times:
                    mylogs.log_info('****Has interval time for {} seconds****'.format(sleep_times))
                    sleep(sleep_times)
                    self.k.tap_key(self.k.tab_key)
                else:
                    mylogs.log_info('****No interval time****')
                    self.k.tap_key(self.k.tab_key)
        except Exception as e:
            raise e


    @get_func_name
    def click_space_key(self,sleep_times,run_times=0,*args):
        try:
            if run_times:

                run = run_times

            else:
                run = self.click_times

            mylogs.log_info('clicking space key will be executed %d times' % run)

            for _ in range(0,run):
                if sleep_times:
                    mylogs.log_info('****Has interval time for {} seconds****'.format(sleep_times))
                    sleep(sleep_times)
                    self.k.tap_key(self.k.space)
                else:
                    mylogs.log_info('****No interval time****')
                    self.k.tap_key(self.k.space)
        except Exception as e:
            mylogs.log_error('Error happen while clicking space key')
            raise e
 
    @get_func_name
    def press_ctrl_keys(self,key_name,sleep_times,run_times=0,*args):

        """
        @ param: key_name - [A-Z]
        @ param: sleep_times - interval time between last click and next click atction
        @ param: run_times - press or click times totally
        """
        try:
            if run_times:

                run = run_times

            else:
                run = self.click_times

            mylogs.log_info('pressing ctrl key will be executed %d times' % run)

            for _ in range(0,run):
                if sleep_times:
                    mylogs.log_info('****Has interval time for {} seconds****'.format(sleep_times))
                    sleep(sleep_times)
                    self.k.press_key(self.k.control_key)
                    self.k.tap_key(key_name)
                    self.k.release_key(self.k.control_key)
                else:
                    mylogs.log_info('****No interval time****')
                    self.k.press_key(self.k.control_key)
                    self.k.tap_key(key_name)
                    self.k.release_key(self.k.control_key)
        except Exception as e:
            mylogs.log_error('Error happen while press ctrl + {} keys'.format(key_name))
            raise e

   # @staticmethod
    def click_enter_key(self):
        """
        click enter key from keyboard
        """
        print("Start to press enter key")
        sleep(2)
    	self.k.tap_key(self.k.enter_key)
        sleep(1)
        print("press enter key second time")
        self.k.tap_key(self.k.enter_key)
        

    def click_esc_key(self):
        pass


    @staticmethod
    @get_func_name
    def test_decorator():

        mylogs.log_info('test decorator')

    # @staticmethod
    def click_connect_btn(self):

        mylogs.log_info('****Start to click connect button****')

        try:

            self.click_tab_key(1,2)
            sleep(2)
            self.click_space_key(1,1)
            # sleep(1)
            # self.click_tab_key(1,1)
            # self.click_space_key(1,1)

        except Exception as e:

            mylogs.log_error('Error occurs due to {}'.format(e))

            raise e


    def close_all_terminals(self):

        mylogs.log_info('****Start to close all terminals****')

        try:


            self.press_ctrl_keys('d',1)  # close ota monitor terminal

            sleep(1)

            self.press_ctrl_keys('c',1)  # close esync client terminal

            sleep(1)

            self.press_ctrl_keys('c',1)  # close uds server terminal

            sleep(1)

            self.press_ctrl_keys('d',1)

            sleep(1)

            self.press_ctrl_keys('d',1) # close setup dm tree terminal

            mylogs.log_info('Close all terminal include uds and esync and monitor')

        except Exception as e:

            mylogs.log_error('Error occur due to {}'.format(e))

            raise e

    def click_download_and_install_btn(self):
        """
        step1: click download button
        step2: click install button
        """
        mylogs.log_info('****Start to click download button****')

        self.m.click(250,500,1)

        sleep(2)

        mylogs.log_info('****Start to click installation button****')

        self.m.click(600,500,1)


    def click_close_btn(self):
        """
        close ota monitor hmi window
        """
        mylogs.log_info('****Start to click close button****')
        try:
            self.m.click(745,65,1)
        except Exception as e:
            mylogs.log_error('Error occur due to {}'.format(e))
            raise e
        else:
            pass
        finally:
            pass


    def take_screen_shot(self):

        try:
            os.system('gnome-screenshot -wb')

            mylogs.log_info('****Get screen_shot****')

        except Exception as e:

            mylogs.log_error("Error happen while taking screen_shot due to {}".format(e))








if __name__ == "__main__":		
    # UserActivity.click_enter_key()
    sleep(5)
    user = UserActivity()
    # user.operate_ota_monitor()
    user.click_enter_key()
