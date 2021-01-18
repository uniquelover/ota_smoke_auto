#!/usr/bin/env python

"""
@ name: createsouit.py
@ Usage: Sync xml and test suite before luanch framework test case.
@ Created on: 1/12/2021
@ Author: tiankang <kang.tian@excelfore-china.com>
"""

import os
from time import sleep
from functools import wraps
from xmlparse import *
import shutil





class CreateProjetSuit:


    def __init__(self,xml_name):

        self.project_path = "/home/autotest/Downloads/OtaSmoke/testcases/smoke"

        self.xmlparse = XMLParse(xml_name)
        

    def get_xml_files(self):

        xmllists = self.xmlparse.get_all_files()

        print(len(xmllists))

        if len(xmllists) == 0:

            print('No any test case in xml please check it again')

            return

        # print(xmllists)

        return xmllists

    def check_test_suite(self,project_name):

        self.test_suite = "test_{}_smoke".format(project_name)

        print(self.test_suite)
        if os.path.exists(self.project_path+'/'+project_name+'/'+self.test_suite):
            print('{} exists already'.format(self.test_suite))
        else:
            os.mkdir(self.project_path+'/'+project_name+'/'+self.test_suite)

        test_files = []


        for tf in self.find_all_files(self.project_path+'/'+project_name+'/'+self.test_suite):

            if tf.endswith('.py') and tf.startswith('test'):

                test_files.append(tf)

        print(test_files)

        return test_files,len(test_files)


    def find_all_files(self,path):

        for root,ds,fs in os.walk(path):

            for f in fs:

                yield f


    def sync_xml_and_suite(self,project_name):

        xmllist = self.get_xml_files().values()  # key: filename

        fn = self.get_xml_files().keys()  # key: path

        xmlfilenum = len(self.get_xml_files())

        suitelist = self.check_test_suite(project_name)  # shijiwenjian 

        src_path = self.project_path[:-5]

        self.test_suite = "test_{}_smoke".format(project_name)

        dest_path = self.project_path + '/' + project_name + '/' + self.test_suite + '/'

        # print('suitelist is {}'.format(suitelist))  # ['test_create_folder.py', 'test_download.py', 'test_download1.py']

        # print('xmlist is {}').format(xmllist)  # ['test_download.py', 'test_create_folder.py']


        if xmllist:

            if suitelist[1] == 0:

                print('test suite no test files and sync it from xml list now')


                for x,y in zip(fn,xmllist):

                    shutil.copy(src_path+x,dest_path)

            else:

                if suitelist[1] == xmlfilenum:

                    for tarfile in suitelist[0]:

                        print(tarfile)

                        if tarfile in xmllist:

                            print("**********xml is the same with test suite***********")

                        else:

                            print("suite {} is not same with xml".format(tarfile))
                            os.remove(dest_path+tarfile)

                    for tarfile1 in xmllist:

                        if tarfile1 not in suitelist[0]:

                            print(tarfile1)

                            for ipath in fn:

                                if ipath.split('/')[-1] == tarfile1:

                                    shutil.copy(src_path+ipath,dest_path)
                else:


                    for tarfile2 in suitelist[0]:

                        print(tarfile2)

                        os.remove(dest_path+tarfile2)

                    for x,y in zip(fn,xmllist):

                        shutil.copy(src_path+x,dest_path)



if __name__ == '__main__':
    cp = CreateProjetSuit('campaign_OTA_simulation.xml')
    cp.sync_xml_and_suite('dongfeng')
