#!/bin/bash

# Name: set_syncclient_teriminal

# Usage: set_env, change_path, close_terminal, execute_sync_client

# ./




function change_path(){
    
    default_path=$(pwd)

    echo 'now work directions is:'  $default_path
    
    script_path="/home/tiankang/Downloads/data"

    cd $script_path

    echo 'new directions is:'  $script_path

	

}


function run_setup_dmtree(){


	./hs_setup_dmtree.sh
}




change_path

sleep 2

run_setup_dmtree
