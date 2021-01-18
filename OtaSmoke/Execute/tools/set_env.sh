#!/bin/bash


function set_env(){
	echo 'set environment'
	export ESYNC_HOME_DIR=/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin
	sleep 2
	export LD_LIBRARY_PATH=/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin/lib
	echo 'set environment completed'


}


# function call_python(){
# 	eval $(./foo.py) && echo $ESYNC_HOME_DIR

# }

function change_path(){
    
    default_path=$(pwd)
	echo 'now work directions is:'  $default_path
    doip_folder="/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin/doip"
    update_file="/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin/doip/update.zip"
    path="/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin/"

	cd $path

	if [ ! -d "$doip_folder" ]; then
		echo "no this folder named doip and create it now"
		mkdir -p doip

	else
		echo "folder doip exists"

	fi

	sleep 3

    if [ ! -f "$update_file" ]; then
		echo "no this file named update.zip and create it now"
		touch doip/update.zip

	else
		echo "file update.zip exists"

	fi



	sleep 3

	cd $default_path

	

}


set_env

change_path

# call_python
