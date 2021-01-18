#!/usr/bin/env python


try:  
    from shlex import quote
except ImportError:  
    from pipes import quote

import subprocess
import shlex
import datetime
from time import sleep
# import virtkey
import os



def run_cmd(cmd, cwd=None, timeout=None, shell=False):

    if shell:
        ccmd = cmd
    else:
        ccmd = shlex.split(cmd)

    print('execute command {}'.format(ccmd))
    sleep(3)
    end_time = 0

    if timeout:

        end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

    
    sub = subprocess.Popen(ccmd, cwd=cwd, stdin=subprocess.PIPE, shell=shell, bufsize=4096)

    while sub.poll() is None:
        sleep(0.5)
        if timeout:
            if end_time <= datetime.datetime.now():
                raise Exception('Timeout {}'.format(ccmd))
    return str(sub.returncode)


def open_terminal():

    v = virtkey.virtkey()
    v.press_keysym(65507)  
    v.press_keysym(65505)  
    v.press_unicode(ord('t'))
    sleep(0.1)
    v.release_unicode(ord('t'))
    v.release_keysym(65507)
    v.release_keysym(65505)


def switch_terminal():

    v = virtkey.virtkey()
    v.press_keysym(65507)  
    v.press_keysym(65366)  
    sleep(0.1)
    v.release_keysym(65507)
    v.release_keysym(65366)

def send_tab_key():

    v = virtkey.virtkey()
    sleep(2)
    print('click tab key two times')
    v.press_keysym(65289) 
    v.release_keysym(65289) 
    v.press_keysym(65289) 
    v.release_keysym(65289) 
    print('end to click')


def launch_udsserver_terminal():

    print('Start to launch udsserver')

    os.system("gnome-terminal -t udsserver -e 'bash -c \"source ./launch_udsserver_terminal.sh; exec bash\"'")


def launch_syncclient_terminal():
    print('Start to launch esyncclient')

    os.system("gnome-terminal -t syncclient -e 'bash -c \"source ./launch_esyncclient_terminal.sh; exec bash\"'")


def launch_otamonitor_terminal():

    print('Start to launch otamonitor')

    os.system("gnome-terminal -t otamonitor -e 'bash -c \"source ./launch_otamonitor_terminal.sh; exec bash\"'")    


def check_env():

    if os.environ['ESYNC_HOME_DIR'] == '/home/autotest/Downloads/Excelforepackage/excelfore/esync':
        print('Set ESYNC HOEM DIR successfully')
        return True
    else:
        print('Failed to set ESYNC HOEM DIR')
        return False

def set_ubuntu_env():

    esync_path = '/home/autotest/Downloads/Excelforepackage/excelfore/esync'
    print('export ESYNC_HOME_DIR={}'.format(quote(esync_path)))

    sleep(3)

    if os.environ['ESYNC_HOME_DIR'] == '/home/autotest/Downloads/Excelforepackage/excelfore/esync':
        print('set ESYNC_HOME successfully')

    else:
        print('failed to set ESYNC_HOME')


def check_result(campaign_path):

    # campaign_path = "/home/autotest/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator"
    folder_num = 0 
    current_time = datetime.datetime.now()
    all_folder = []

    if os.path.exists(campaign_path):

        dirlist = os.listdir(campaign_path)

        print(dirlist)


        if dirlist is not None:

            for x in dirlist:

                if os.path.isdir((os.path.join(campaign_path,x))):

                    return True
                else:

                    return False

                    # print(x + ' ' + "is folder")

                    # folder_num += 1

                    # all_folder.append((os.path.join(campaign_path,x)))

    # return all_folder



def find_newest_folder(path_file):
    lists = os.listdir(path_file)
    lists.sort(key=lambda fn: os.path.getmtime(path_file +'/'+fn))
    # print(lists)
    for x in reversed(lists):
        if os.path.isdir((os.path.join(path_file,x))):
            # print(x)
            floder_newest = os.path.join(path_file,x)
            break
    return floder_newest
    

def check_update_res():
    path_file = "/home/autotest/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator"
    state_path = '/State/value'
    if find_newest_folder(path_file):
        value_path = find_newest_folder(path_file) + state_path
        with open(value_path,'r') as f:
            vaule_data = f.read()
            # print(vaule_data)
    if vaule_data == "90":
              print('---Ota update successfully---')
              return True
    else:
        print('---Failed to update ota---')
        return False




if __name__ == '__main__':

#    execute_cmd('cat test.py')
#    set_environment('ESYNC_HOME_DIR','/home/excelfore/Documents/excelfore/esync')
    # setEnv()
    # run_cmd('export ESYNC_HOME_DIR=/home/excelfore/Documents/excelfore/esync',cwd='/home/autotest/Downloads', timeout=2, shell=True)
    # run_cmd('./set_env.sh', timeout=2, shell=True)
    # run_cmd('eval $(./foo.py) && echo $ESYNC_HOME_DIR', timeout=2, shell=True)
    # run_cmd('gnome-terminal -e ls', shell=True)

    # run_cmd('env | grep ESYNC_HOME_DIR',cwd='/home/autotest/Downloads', timeout=2, shell=True)

    # open_terminal()
    # sleep(3)
    # # run_cmd('eval $(./set_ubuntu_env.py) && echo $ESYNC_HOME_DIR', timeout=2, shell=True)
    # switch_terminal()
    # sleep(2)
    # run_cmd('./set_env.sh', shell=True)
    # set_ubuntu_env()
    # sleep(2)
    # check_env()
    # launch_udsserver_terminal()
    # sleep(5)
    # launch_syncclient_terminal()
    # sleep(1)
    # 
    # check_result()
    # get_latest_folder()
    # dir = "/home/autotest/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator"
    # new_report(path)
    # print(find_newest_folder(dir))
    check_update_res()
