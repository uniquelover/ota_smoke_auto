#!/usr/bin/env python3

"""
@ name:common_helper.py
@ time: 12/7/2020
@ function: Some common functions for ota download package

__author__='kang'
__version__='v1.0'
"""


import sys
sys.path.append('/home/autotest/Downloads/OtaSmoke/Mylog')
import requests
import os
from time import sleep
from logs import GetLogs
import datetime
import shlex
import subprocess
# sys.path.append('/home/autotest/Downloads/OtaSmoke/Mylog')
# sys.path.append(r'D:\\TestPython\\Mylog')


mylogs = GetLogs()


def create_path():
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
        default_path_lin = '/home/autotest/Downloads/Excelforepackage'
        if not judge_path():
            try:
                os.makedirs(default_path_lin, 0777)
                sleep(1)
                mylogs.log_info('Target folder has been created on linux')
                return True
            except:
                mylogs.log_error('Failed to creat folder')


def judge_path():  # TODO: Judge weather the path to save ota auto release exists or not.
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
        lin_path = '/home/autotest/Downloads/Excelforepackage'
        folder = lin_path.split('/')[-1]
        if os.path.exists(lin_path) == True:
            mylogs.log_info('Target folder named {0} exists'.format(folder))
            return True
        else:
            mylogs.log_error('Target folder named {0} not exists'.format(folder))
            return False


def download_release():  # TODO: Download the latest release from url given by developer.
    response_code = None



    url = 'http://dev.excelfore-china.com:82/esyncrelease/esync_client_release/CEE/V20.12.3.0/excelfore_x86_' \
          '64_esync_client_evo_release_2020.12.4.23.8.tar.gz'
    try_times = 0
    total_times = 3
    if judge_path():
        # res = requests.get(url)
        # response_code = res.status_code
        while try_times < total_times:
            mylogs.log_info('Download package for %d times' % (try_times + 1))
            res = requests.get(url)
            response_code = res.status_code
            if response_code == 200:
                mylogs.log_info('Download latest release file successfully')
                if parser_web_path:
                    release_name = parser_web_path(url)
                    save_path = os.path.join('/home/autotest/Downloads/Excelforepackage', release_name)
                    try:
                        with open(save_path, 'wb') as f:
                            f.write(res.content)
                        return True
                    except Exception as e:
                        mylogs.log_error("There has a error : %s" % e)
                        return False
                    # finally:
                    #     f.close()
                break
            # else:
            #     mylogs.log_error('download package three times failed')
            #     return
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


def parser_web_path(url=None):
    """
    @ params:url
    @ return: str
    """
    url = 'http://dev.excelfore-china.com:82/esyncrelease/esync_client_release/CEE/V20.12.3.0/' \
          'excelfore_x86_64_esync_client_evo_release_2020.12.4.23.8.tar.gz'

    res = url.split("/")[-1]
    print(res)
    return res
 

def delete_release():
    pass


def get_pwd():
    current_path = os.getcwd()
    print(current_path)
    return current_path


def extract_package():
    module = 'tarfile'
    f = __import__(module)
    # import tarfile
    if parser_web_path:
        release_name = parser_web_path()
        # target_path = r'C:\Users\Administrator\Downloads\Excelforepackage'  # windows
        target_path = '/home/autotest/Downloads/Excelforepackage'  # linunx
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

    print('execute command {}'.format(ccmd))
    sleep(3)
    end_time = 0
    if timeout:

        end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

    if cwd:
        print('command run in {}'.format(cwd))
    else:
        print('-------no cwd---------')

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

    if os.name == 'posix':
        return 'Linux'
    if os.name == 'nt':
        return 'Windows'


def get_python_version():
    pass


def change_work_path():
    pass


def check_env():

    if os.environ['ESYNC_HOME_DIR'] == '/home/autotest/Downloads/Excelforepackage/excelfore/esync':
        mylogs.log_info('Set ESYNC HOEM DIR successfully')
        return True
    else:
        mylogs.log_error('Failed to set ESYNC HOEM DIR')
        return False


def get_newest_folder(path_file):
    lists = os.listdir(path_file)
    lists.sort(key=lambda fn: os.path.getmtime(path_file +'/'+fn))
    # print(lists)
    for x in reversed(lists):
        if os.path.isdir((os.path.join(path_file,x))):
            # print(x)
            floder_newest = os.path.join(path_file,x)
            break
    return floder_newest
    

def check_update_res(path_file=None):
    path_file = "/home/autotest/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator"
    state_path = '/State/value'
    if get_newest_folder(path_file):
        value_path = get_newest_folder(path_file) + state_path
        with open(value_path,'r') as f:
            vaule_data = f.read()
    if vaule_data == "90":
              mylogs.log_info('---Ota update successfully---')
              return True
    else:
        mylogs.log_error('---Failed to update ota---')
        return False
        

if __name__ == "__main__":

    # parser_web_path()
    # get_pwd()
    # judge_path()
    # create_path()
    # download_release()
    # extract_package()
    # run_cmd('python')
    check_update_res()