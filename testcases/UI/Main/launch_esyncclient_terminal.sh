#!/bin/bash

# Name: set_syncclient_teriminal

# Usage: set_env, change_path, close_terminal, execute_sync_client

# ./esyncclient -p ../etc/policies.json -t ../data/dm_tree/



function set_env(){

	echo 'set temporary environment variable'
	export ESYNC_HOME_DIR=/home/autotest/Downloads/Excelforepackage/excelfore/esync
	sleep 2
	export LD_LIBRARY_PATH=/home/autotest/Downloads/Excelforepackage/excelfore/esync/lib
	echo 'set temporary environment variable completed'


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

	set_path="ESYNC_HOME_DIR=/home/autotest/Downloads/Excelforepackage/excelfore/esync/bin"

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


function execute_esync_client(){

	./esyncclient -p ../etc/policies.json -t /home/autotest/Downloads/dm_tree/


}




set_env

sleep 5

change_path

check_env

sleep 2

execute_esync_client

# change_path

# close_terminal

# call_python

