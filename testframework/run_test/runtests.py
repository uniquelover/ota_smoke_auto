#!/usr/bin/env python

"""
@ Usage: This module is used to operate pytest framework
@ Nmae:  runcase.py
@ Create on: 1/12/2021
@ Author:tiankang <kang.tian@excelfore-china.com>
# """


import sys
import pytest
import os
from time import sleep




def load_settings():

    pass



def main(testsuite,htmlpath,outhtml=True):

    cmd = 'pytest -s'

    if outhtml:
        
        print('------Start to launch pytest framework-----')
        os.system(cmd + ' ' + testsuite + ' ' + htmlpath)

    else:
        print('No html file outputting')
        try:
            os.system(cmd + ' ' + testsuite)
        except Exception as e:

            raise e

        finally:

            print('Pytest running finished ')

            return True


if __name__ == '__main__':
    
    main('/home/tiankang/Downloads/OtaSmoke/testcases/smoke/dongfeng/test_dongfeng_smoke','--html=/home/tiankang/Downloads/OtaSmoke/Logs/dongfeng/test_dongfeng_ota_smoke.html')