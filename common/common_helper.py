#!/usr/bin/env python3

"""
@ ----------------------------------------------------
@ Name:common_helper.py
@ Created on: 12/7/2020
@ Usage: Some common functions for ota auto test
@ author: tiankang <kang.tian@excelfore-china.com>
@ version: v1.0dongfeng
@ ----------------------------------------------------
"""


import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
# sys.path.append('../Mylog')
import requests
import os
from time import sleep
from logs import GetLogs
import datetime
import shlex
import subprocess
import configparser


mylogs = GetLogs()


def create_path(default_path_lin='/home/tiankang/Downloads/Excelforepackage',file_name=None,need_create_file=False):

    if get_platform() == 'Windows':
        default_path_win = r'C:\\Users\\Administrator\\Downloads\\Excelforepackage'
        if not judge_path():
            try:
                os.makedirs(default_path_win)
                sleep(1)
                mylogs.log_info('Target folder has been created on windows')
                return True
            except:
                mylogs.log_error('Failed to creat folder')
    if get_platform() == 'Linux':
        if not judge_path(default_path_lin):
            try:
                os.makedirs(default_path_lin, 0777)
                sleep(1)
                mylogs.log_info('Target folder named {} has been created on linux'.format(default_path_lin.split('/')[-1]))
                if need_create_file:
                    mylogs.log_info('Need to create zip files')
                    if not os.path.exists(default_path_lin + '/' + file_name):
                        os.chdir(default_path_lin)
                        os.mkdir(file_name)
                        mylogs.log_info('zip file has been created ')
                        return True
                return True
            except:
                mylogs.log_error('Failed to creat folder')
        else:

            mylogs.log_info('Excelforepackage folder exists')
            return True


def judge_path(lin_path='/home/tiankang/Downloads/Excelforepackage'):

    if get_platform() == 'Windows':
        win_path = r'C:\\Users\\Administrator\\Downloads\\Excelforepackage'
        folder = win_path.split('\\')[-1]
        if os.path.exists(win_path):
            mylogs.log_info('Target folder named {0} exists'.format(folder))
            return True
        else:
            mylogs.log_error('Target folder named {0} not exists'.format(folder))
            return False
    if get_platform() == 'Linux':
        folder = lin_path.split('/')[-1]
        if os.path.exists(lin_path) == True:
            mylogs.log_info('Target folder named {} exists'.format(folder))
            return True
        else:
            mylogs.log_info('Target folder named {} not exists'.format(folder))
            return False


def parser_ini(inikey,inivaluse):

        ini_file = "test_cfg.ini"
        config = configparser.ConfigParser()
        if os.path.exists(ini_file):
            config.read(ini_file)
            convaluse=config.get(inikey,inivaluse)
            return convaluse.encode("utf-8")
        else:
            mylogs.log_error('no ini config file')
            return False


def download_release(pkg_save_path='/home/tiankang/Downloads/Excelforepackage'):  

    # TODO: Download the latest release from url given by developer.

    response_code = None

    url = parser_ini('releaseinfo','url')

    try_times = 0
    total_times = 3
    if judge_path():
        while try_times < total_times:
            mylogs.log_info('Download package for %d times' % (try_times + 1))
            res = requests.get(url)
            response_code = res.status_code
            if response_code == 200:
                mylogs.log_info('Download latest release file successfully')
                if parser_web_path:
                    release_name = parser_web_path()
                    save_path = os.path.join(pkg_save_path, release_name)
                    try:
                        with open(save_path, 'wb') as f:
                            f.write(res.content)
                        return True
                    except Exception as e:
                        mylogs.log_error("There has a error : %s" % e)
                        return False
                break
            sleep(3)
            try_times += 1
        if response_code != 200 and try_times == 3:
            mylogs.log_error('Download package for 3 times but failed...')
            return False
        # print(response_code)
        # if response_code == 200:
        #     # mylogs.log_info('download latest release file successfully')
        #     if parser_web_path:
        #         release_name = parser_web_path(url)
        #         save_path = os.path.join(r'C:\Users\Administrator\Downloads\Excelforepackage',release_name)
        #         try:
        #             with open(save_path, 'wb') as f:
        #                 f.write(res.content)
        #         except Exception as e:
        #                 mylogs.log_error("There is a error : %s" %e)
        #                 return
        #         finally:
        #             f.close()
        # else:
        #     mylogs.log_error('download package three times feiled')
        #     return
    else:
        mylogs.log_info('No path named excelforepackage and create it now')
        create_path()
        res = requests.get(url)
        mylogs.log_info('Download latest release file')
        try:
            with open('Excelfore_x86_64_esync_client_evo_release_2020.12.4.23.8.tar.gz', 'wb') as f:
                f.write(res.content)
        except Exception as e:
            mylogs.log_error("There has an error : %s" % e)
            return
        finally:
            f.close()


def parser_web_path():
    """
    @ param: url
    @ returns: str
    """
    # url = 'http://dev.excelfore-china.com:82/esyncrelease/esync_client_release/CEE/V20.12.3.0/' \
    #       'excelfore_x86_64_esync_client_evo_release_2020.12.4.23.8.tar.gz'
    
    if get_latest_release():

        res = get_latest_release().split("/")[-1]
        mylogs.log_info(res)
        return res
 

def get_pwd():
    current_path = os.getcwd()
    mylogs.log_info(current_path)
    return current_path


def extract_package():

    module = 'tarfile'
    f = __import__(module)
    # import tarfile
    if get_latest_release:
        release_name = get_latest_release('/home/tiankang/Downloads/Excelforepackage')
        target_path = '/home/tiankang/Downloads/Excelforepackage'  
        target_file = os.path.join(target_path, release_name)
        extract_file_name = os.path.join(target_path, 'excelfore')
        if os.path.exists(target_file):
            try:
                tar_files = f.open(target_file, 'r')
                tar_files.extractall(target_path)
                sleep(3)
                try:
                    if os.path.exists(extract_file_name):
                        mylogs.log_info('Extract file %s successfully' % release_name)
                        return True
                except Exception as e:
                    mylogs.log_error('Error occur while extracting tar.gz due to %s: ' % e)

            except Exception as e:
                mylogs.log_error('Something wrong while extracting tar.gz due to %s: ' % e)
                return False
        else:
            mylogs.log_error('No this package file')
            return False


def run_cmd(cmd, cwd=None, timeout=None, shell=False):
    """
    param: cmd, the command will be executed
    param: cwd, the work direction where command executed
    param: timeout, set time when executing command
    param: shell, will use linux shell mode if set True
    """
    import subprocess
    import shlex
    mylogs.log_info('Executing command:' + ' ' + cmd)
    try:
        if shell:
            ccmd = cmd
        else:
            ccmd = shlex.split(cmd)
        proc = subprocess.Popen(ccmd, shell=shell)
        proc.wait()
        if proc.returncode != 0:
            raise Exception('Execute command return value was not 0!')
    except Exception as e:
        mylogs.log_info('---------FAILURE MESSAGE-------')
        mylogs.log_info('Error message is %s' % e)
        mylogs.log_info('---------FAILURE MESSAGE-------')


def run_cmds(cmd, cwd=None, timeout=None, shell=False):

    if shell:
        ccmd = cmd
    else:
        ccmd = shlex.split(cmd)

    mylogs.log_info('execute command {}'.format(ccmd))
    sleep(3)
    end_time = 0
    if timeout:

        end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

    if cwd:
        mylogs.log_info('command run in {}'.format(cwd))
    else:
        mylogs.log_info('-------no cwd---------')

    sub = subprocess.Popen(ccmd, cwd=cwd, stdin=subprocess.PIPE, shell=shell, bufsize=4096)

    while sub.poll() is None:
        sleep(0.5)
        if timeout:
            if end_time <= datetime.datetime.now():
                raise Exception('Timeout {}'.format(ccmd))
    return str(sub.returncode)


def set_ubuntu_env():

    cmd = 'eval $(./set_ubuntu_env.py)'
    try:

        run_cmds(cmd, timeout=5, shell=True)
    except Exception as e:
        mylogs.log_error('failed to call rum cmd method ')
        raise e

    sleep(2)
    if os.environ['ESYNC_HOME_DIR'] == '/home/excelfore/Documents/excelfore/esync' and \
            os.environ['LD_LIBRARY_PATH'] == '/home/excelfore/Documents/excelfore/esync/lib':
        mylogs.log_info('set ESYNC_HOME successfully')
        return True

    else:
        mylogs.log_error('failed to set ESYNC_HOME and LD_LIBRARY_PATH')
        return False


def get_platform():
    """
    only run scripts on windows and linux now.
    """

    if os.name == 'posix':
        return 'Linux'
    if os.name == 'nt':
        return 'Windows'


def check_env():

    if os.environ['ESYNC_HOME_DIR'] == '/home/tiankang/Downloads/Excelforepackage/excelfore/esync':
        mylogs.log_info('Set ESYNC HOEM DIR successfully')
        return True
    else:
        mylogs.log_error('**********Failed to set ESYNC HOEM DIR*******************')
        return False


def get_newest_folder(path_file):

    lists = os.listdir(path_file)
    lists.sort(key=lambda fn: os.path.getmtime(path_file +'/'+fn))
    for x in reversed(lists):
        if os.path.isdir((os.path.join(path_file,x))):
            floder_newest = os.path.join(path_file,x)
            break
    return floder_newest
    

def check_update_res_campaign(path_file=None):

    path_file = "/home/tiankang/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator"
    state_path = '/State/value'
    if get_newest_folder(path_file):
        value_path = get_newest_folder(path_file) + state_path
        with open(value_path,'r') as f:
            value_data = f.read()
    # if value_data == "90" or value_data == "100":
    #           mylogs.log_info('Ota update successfully')
    #           return True
    while True:
        if value_data == "90" or value_data == "100":
            mylogs.log_info('Ota update successfully')
            return True
        else:
            mylogs.log_error('Failed to update ota')
            return False
        sleep(10*3)
    # else:
    #     mylogs.log_error('Failed to update ota')
    #     return False


def check_update_res_fumo(path_file=None):

    path_file = "/home/tiankang/Downloads/data/dm_tree/FUMO/"
    fumo = ['7905071-DB01-0x0011','7905072-DB02-0x0012','7905073-DB03-0x0013']
    state_path = '/Ext/State/6/State/value'


    whole_path = []

    for i in fumo:

        whole_path.append(path_file+i+state_path)


    print(whole_path)

    total_num = 0

    for k in whole_path:

        with  open(k,'r') as f:

            value_data = f.read()

        if value_data == "90" or value_data == "100":

            mylogs.log_info('Ota update successfully at {}'.format(k))

            total_num += 1

    if total_num == 3:

        mylogs.log_info("All packages update successfully")

        return True

    else:

        mylogs.log_error('Some packages or all packages update failed')

        return False











    # if get_newest_folder(path_file):
    #     value_path = get_newest_folder(path_file) + state_path
    #     with open(value_path,'r') as f:
    #         value_data = f.read()
    # while True:
    #     if value_data == "90" or value_data == "100":
    #         mylogs.log_info('Ota update successfully')
    #         return True
    #     else:
    #         mylogs.log_error('Failed to update ota')
    #         return False
    #     sleep(10*3)



def get_latest_release(release_path):

    if len(os.listdir(release_path)) > 0:
        for i in os.listdir(release_path):
            if os.path.isfile(os.path.join(release_path,i)):
                if i.endswith('gz') and i.startswith('excelfore_x86_64'):
                    mylogs.log_info(i)
                    return i
    else:
        mylogs.log_error('No files and folder')
        return False



if __name__ == "__main__":

    # parser_web_path()
    # get_pwd()
    # target_path = "/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/doip"
    # create_path(target_path,'update.zip',True)
    # download_release()
    # print(res)
    # extract_package()
    # run_cmd('python')
    # check_update_res()
    # parser_ini('releaseinfo','url')
    # test_uicode_to_str()
    # judge_path()
    # create_path()
    # print(get_newest_folder('/home/tiankang/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator'))
    # get_latest_release('/home/tiankang/Downloads/Excelforepackage')
    check_update_res_fumo()