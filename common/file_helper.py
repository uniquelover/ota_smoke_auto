# module for some file operate methods


import sys
sys.path.append('/home/tiankang/Downloads/OtaSmoke/Mylog')
# sys.path.append('../Mylog')
from logs import GetLogs
import os
from time import sleep
import tarfile



mylogs = GetLogs()


class OtaFileOperate:

    def create_file(self):
        pass


    def extract_package(self,target_path):
        module = 'tarfile'
        f = __import__(module)
        if parser_web_path:
            release_name = parser_web_path()
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
            mylogs.log_error('No this package')
            return False

    @staticmethod
    def check_extract_package(bin_path):

        # target_files = ['esyncclient', 'doip', 'dmserver', 'uds_server_testappli', 'otamonitor']
        target_files = ['esyncclient', 'dmserver', 'uds_server_testappli', 'otamonitor']
        target_num = 0

        if len(os.listdir(bin_path)) == 4:

            for x in os.listdir(bin_path):

                if x in target_files:

                    mylogs.log_info(x)

                    target_num += 1

        if target_num == 4:

            return True

        else:

            return False


    @staticmethod
    def delete_file_or_folder(path,num=None):

        """
        @ params: path,str,the path of folder or file want to delete
                  num, int, delete some file or total folder
        @ retures: bool       
        """

        print('start to delete ....')

        if os.path.isfile(path):

            name = 'file'

        else:

            name = 'folder'

        if os.path.exists(path):


            if num == "na":

                print("Delete some files or folders only")

            for i in os.listdir(path):
                if not i.endswith('.xml'):
                    print(i)
                    os.system('rm -rf ' + ' ' + os.path.join(path,i))

                sleep(1)



            del_num = 0

            for m in os.listdir(path):
                if not os.path.exists(os.path.join(path,m)):
                    mylogs.log_info('Delete {} successfully'.format(m))
                    del_num += 1
            
            if del_num == len(os.listdir(path)):
                return True



            if num == "all":

                print("Total folder will be deleted")

                os.system('rm -rf' + ' ' + path)


                if not os.path.exists(path):

                    mylogs.log_info('Delete {0} named {1} successfully'.format(name,path.split('/')[-1]))

                    return True

                else:

                    mylogs.log_error('Failed to delete {0} named {1}'.format(name,path.split('/')[-1]))

                    return False


        else:

            print('no path')
        
            mylogs.log_error('No this {0} location at {1}'.format(name,path))

            return False    

        # if not os.path.exists(path) or os.path.exists():

        #     mylogs.log_info('Delete {0} named {1} successfully'.format(name,path.split('/')[-1]))

        #     return True

        # else:

        #     mylogs.log_error('Failed to delete {0} named {1}'.format(name,path.split('/')[-1]))

        #     return False



def filter():

    esync_log = '/home/tiankang/Downloads/OtaSmoke/Logs/esynclog/run.log'
    esync_err_log = '/home/tiankang/Downloads/OtaSmoke/Logs/esynclog/err.txt'

    try:

        with open(esync_log,'r') as fo:

            listfile = fo.readlines()

#            print(listfile)

            print("run.log has {} lines totally".format(len(listfile)))


        if listfile is not None:

            f = open(esync_err_log,'a')
            
            err_num = 0

            for i in range(0,len(listfile)):

#                print(i)
#                print(len(listfile[i].split(" ")))

                if len(listfile[i].split(" ")) < 9:
            
                    continue


                if listfile[i].split(" ")[4]  == "[ERR]":

                    mylogs.log_error(listfile[i])

                    print(listfile[i].split(" ")[6])

                    f.write(listfile[i])

                    err_num += 1

#            sp(1)

            f.close()

        mylogs.log_info("Has {} errors totally".format(err_num))

    except Exception as e:

        mylogs.log_error("error happen while filter file due to {}".format(e))




if __name__ == "__main__":

    bin_path = '/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin'
    fumo_path = '/home/tiankang/Downloads/data/dm_tree/FUMO'
    # ota = OtaFileOperate()
    # print(OtaFileOperate.check_extract_package(bin_path))
    # OtaFileOperate.delete_file_or_folder(fumo_path,"na")
    filter()