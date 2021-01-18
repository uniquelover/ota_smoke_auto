# module for some file operate methods



import os
from time import sleep
import tarfile


class OtaFileOperate:

	def create_file(self):
		pass


    def extract_package(self,target_path):
    module = 'tarfile'
    f = __import__(module)
    if parser_web_path:
        release_name = parser_web_path()
        # target_path = '/home/autotest/Downloads/Excelforepackage'
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

