#!/bin/bash

# Name: launch_otamonitor_teriminal

# Usage: set_env, change_path, close_terminal, execute_sync_client

# ./esyncclient -p ../etc/policies.json -t /home/tiankang/Downloads/dm_tree/

# Version: x86 v1.0

# Date: 12/30/2020

# Authored by kang.tian <kang.tian@excelfore-china.com>



function set_env(){

	# echo 'set temporary environment variable'
	# export ESYNC_HOME_DIR=/home/tiankang/Downloads/Excelforepackage/excelfore/esync
	# sleep 2
	export LD_LIBRARY_PATH=/home/tiankang/Downloads/Excelforepackage/excelfore/esync/lib
	echo 'set temporary environment variable completed'


}




function change_path(){
    
    default_path=$(pwd)
    echo 'now work directions is:'  $default_path
    doip_folder="/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/doip"
    update_file="/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/doip/update.zip"
    path="/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/"

	cd $path

	ls -l



	# if [ ! -d "$doip_folder" ]; then
	# 	echo "no this folder named doip and create it now"
	# 	mkdir -p doip

	# else
	# 	echo "folder doip exists"

	# fi

	# sleep 3

 #    if [ ! -f "$update_file" ]; then
	# 	echo "no this file named update.zip and create it now"
	# 	touch doip/update.zip

	# else
	# 	echo "file update.zip exists"

	# fi



	# sleep 3

	# cd $default_path

	

}

function check_env(){

	sync_path=$(env | grep ESYNC_HOME_DIR)

	set_path="ESYNC_HOME_DIR=/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin"

	echo $sync_path

	# if [ $sync_path = $set_path ]; then

	# 	echo "set env successfully"

	# 	return 0
	# else
	# 	echo "failed to set check_env"

	# 	return 1
}


function close_terminal(){

	echo "terminal will be closed after 5 seconds"

	sleep 5

	exit
}


function launch_ota_monitor(){

	./otamonitor

	# sleep 2

	# python3 /home/tiankang/Documents/script/send_ota_cmd.py


}




set_env

# sleep 1

check_env

change_path

launch_ota_monitor

# sleep 5 


# colse_terminal

# change_path

# close_terminal

# call_python


