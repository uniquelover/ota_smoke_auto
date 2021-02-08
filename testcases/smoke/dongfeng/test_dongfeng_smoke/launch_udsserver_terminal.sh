#!/bin/bash
# name: launch_udsserrver_terminal

# usage: set_env , change_path, create doip and update.zip, execute udsserver, close terminal

# ./uds_server_testappli ../etc/x4doip/config.xml 

function set_env(){
	echo 'set environment'
	export ESYNC_HOME_DIR=/home/tiankang/Downloads/Excelforepackage/excelfore/esync
	sleep 2
	export LD_LIBRARY_PATH=/home/tiankang/Downloads/Excelforepackage/excelfore/esync/lib
	echo 'set environment completed'


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

function create_folder(){
    
    default_path=$(pwd)
    echo 'now work directions is:'  $default_path
    doip_folder="/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/doip"
    update_file="/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/doip/update.zip"
    path="/home/tiankang/Downloads/Excelforepackage/excelfore/esync/bin/"

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



	# sleep 3

	# cd $default_path

	

}


function close_terminal(){

	echo "terminal will be closed after 5 seconds"

	sleep 5

	exit
}


function launch_uds_server(){


	./uds_server_testappli ../etc/x4doip/config.xml 
}


set_env

check_env

create_folder

change_path

launch_uds_server

# close_terminal

