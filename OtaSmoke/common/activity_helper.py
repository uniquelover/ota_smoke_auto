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
import sys
from time import sleep		 





def get_func_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('now execute is %s' % func.__name__)
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

                # print('args.....')

                run = run_times

            else:
                run = self.click_times

            print('clicking tab key will be executed %d times' % run)

            for _ in range(0,run):
                if sleep_times:
                    print('Has interval time****')
                    sleep(sleep_times)
                    self.k.tap_key(self.k.tab_key)
                else:
                    print('*****No interval time')
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

            print('clicking space key will be executed %d times' % run)

            for _ in range(0,run):
                if sleep_times:
                    print('Has interval time****')
                    sleep(sleep_times)
                    self.k.tap_key(self.k.space)
                else:
                    print('*****No interval time')
                    self.k.tap_key(self.k.space)
        except Exception as e:
            print('error while clicking space key')
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

            print('pressing ctrl key will be executed %d times' % run)

            for _ in range(0,run):
                if sleep_times:
                    print('Has interval time****')
                    sleep(sleep_times)
                    self.k.press_key(self.k.control_key)
                    self.k.tap_key(key_name)
                    self.k.release_key(self.k.control_key)
                else:
                    print('*****No interval time')
                    self.k.press_key(self.k.control_key)
                    self.k.tap_key(key_name)
                    self.k.release_key(self.k.control_key)
        except Exception as e:
            print('Error happen while press ctrl + {} keys'.format(key_name))
            raise e

    @staticmethod
    def click_enter_key():
    	UserActivity.k.tap_key(k.space)
        pass         

    def click_esc_key(self):
        pass


    @staticmethod
    @get_func_name
    def test_decorator():

        print('test decorator')

    # @staticmethod
    def operate_ota_monitor(self):

        self.click_tab_key(1,2)
        sleep(2)
        self.click_space_key(1,1)
        sleep(1)
        self.click_tab_key(1,1)
        self.click_space_key(1,1)


    def close_ota_monitor(self):

        try:

            self.press_ctrl_keys('d',1)

            sleep(1)

            self.press_ctrl_keys('c',1)

            sleep(1)

            self.press_ctrl_keys('c',1)

            sleep(1)

            self.press_ctrl_keys('d',1)

            print('Close all terminal include uds and esync and monitor')

        except Exception as e:

            print('Error occur due to {}'.format(e))

            raise e







if __name__ == "__main__":		
    # UserActivity.click_enter_key()
    sleep(5)
    user = UserActivity()
    # user.operate_ota_monitor()
    user.close_ota_monitor()