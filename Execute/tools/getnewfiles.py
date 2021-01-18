import os

def find_newest_file(path_file):
    lists = os.listdir(path_file)
    lists.sort(key=lambda fn: os.path.getmtime(path_file +'/'+fn))
    print(lists)
    file_newest = os.path.join(path_file,lists[-1])
    return file_newest

if __name__ =='__main__':
     file_newest = find_newest_file('/home/autotest/Downloads/dm_tree/DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator')
     print(file_newest)
