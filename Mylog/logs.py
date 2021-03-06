#!/usr/bin/env python3

"""
@ ---------------------------------
@ File:logs.py
@ Created: 12/7/2020
@ Usage: log
@ IDE: VS CODE
@ Python version: 3.7.1
@ Licence: <your licence>
@ ---------------------------------
"""

import logging
import os
import datetime


class GetLogs:

    def __init__(self):
        """
        @ param :None
        @ others:current_time
                 log_path
        """
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        log_path = '/home/tiankang/Downloads/OtaSmoke/Logs'
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        self.logname = os.path.join(log_path, current_time + '.log')
    
    def __set_logs(self, level, message):
        """
        @ param:level set log levels ['debug','info','warning','error','critical]
        @ returns: None
        """

        
        logger = logging.getLogger()
        logger.setLevel("DEBUG")  


        fh = logging.FileHandler(self.logname, 'a', encoding='gbk')
        fh.setLevel('DEBUG')
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')

        
        formatter = logging.Formatter('[%(asctime)s] - [%(lineno)d] - [%(levelname)s] - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        
        logger.addHandler(fh)
        logger.addHandler(ch)

        
        if level == "DEBUG":
            logger.debug(message)
        elif level == "INFO":
            logger.info(message)
        elif level == "WARNING":
            logger.warning(message)
        elif level == "ERROR":
            logger.error(message)
        elif level == "CRITICAL":
            logger.critical(message)
        else:
            raise Exception('Invalid level')

        try:
            logger.removeHandler(fh)
            logger.removeHandler(ch)
            fh.close()
        except Exception as exmsg:
            print(exmsg)

    def log_debug(self, message):
        self.__set_logs('DEBUG', message)

    def log_info(self, message):
        self.__set_logs('INFO', message)

    def log_warning(self, message):
        self.__set_logs('WARNING', message)

    def log_error(self, message):
        self.__set_logs('ERROR', message)
    
    def log_critical(self, message):
        self.__set_logs('CRITICAL', message)


if __name__ == "__main__":

    mylog = GetLogs()
    mylog.log_critical('critical level')
