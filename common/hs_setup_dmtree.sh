#!/bin/bash

declare -A node_value
declare -A node_types
declare -A node_flags

## user can change DevId for test
node_value["DevInfo/DevId"]=urn:excelfore:device:EXCELFORE20201120000000003
node_types["DevInfo/DevId"]=chr
node_flags["DevInfo/DevId"]=V

## user can change VIN for test
node_value["DevInfo/Ext/Excelfore/VIN"]=20201120000000003
node_types["DevInfo/Ext/Excelfore/VIN"]=chr
node_flags["DevInfo/Ext/Excelfore/VIN"]=V

node_value["DevInfo/Ext/Excelfore/Hardware/CurrentVersion"]=DBCBCDCC0000
node_types["DevInfo/Ext/Excelfore/Hardware/CurrentVersion"]=chr
node_flags["DevInfo/Ext/Excelfore/Hardware/CurrentVersion"]=V

## following options may changed by expert
node_value["App/DownloadDir"]=/home/tiankang/disk-temp/esync_download
node_types["App/DownloadDir"]=chr
node_flags["App/DownloadDir"]=V

node_value["App/TmpDir"]=/home/tiankang/disk-temp/esync_app_tmp
node_types["App/TmpDir"]=chr
node_flags["App/TmpDir"]=V

node_value["DevInfo/Ext/Excelfore/CampaignState/ExecutingCampaign"]=2
node_types["DevInfo/Ext/Excelfore/CampaignState/ExecutingCampaign"]=int
node_flags["DevInfo/Ext/Excelfore/CampaignState/ExecutingCampaign"]=V

node_value["DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator/2/State"]=0
node_types["DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator/2/State"]=int
node_flags["DevInfo/Ext/Excelfore/CampaignState/CampaignCorrelator/2/State"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/PkgURL"]=http://192.168.1.118/testdata/manifest-hs-enc.zip
#node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/PkgURL"]=http://192.168.72.21:8080/download/manifest-hs-enc.zip
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/PkgURL"]=chr
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/PkgURL"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadLen"]=0
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadLen"]=int
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadLen"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Length"]=3368
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Length"]=int
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Length"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/EncryptionKey"]=MTIzNDU2Nzg5MDEyMzQ1Ng==
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/EncryptionKey"]=bin
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/EncryptionKey"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/EncryptionMethod"]=AES/CTR/NoPadding
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/EncryptionMethod"]=chr
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/EncryptionMethod"]=V

#node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Sha256"]=8E5n2fUlBCzVIxTTA8GRrsI9B58Tmw2BPvRL6OiLZDA=
node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Sha256"]=n9J/DB9jcOHTIzP7JT/XQ12FE5zRZKI0z8vj1faQkEE=
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Sha256"]=chr
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Sha256"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Correlator"]=2
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Correlator"]=int
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/ManifestInfo/Correlator"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905071-DB01-0x0011/Correlator"]=3
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905071-DB01-0x0011/Correlator"]=int
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905071-DB01-0x0011/Correlator"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905072-DB02-0x0012/Correlator"]=4
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905072-DB02-0x0012/Correlator"]=int
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905072-DB02-0x0012/Correlator"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905073-DB03-0x0013/Correlator"]=4
node_types["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905073-DB03-0x0013/Correlator"]=int
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/DownloadAndUpdate/PkgCorrelator/7905073-DB03-0x0013/Correlator"]=V

node_value["DevInfo/Ext/Excelfore/Campaigns/2/CampaignEnd"]=0
node_types["DevInfo/Ext/Excelfore/Campaigns/2/CampaignEnd"]=boolean
node_flags["DevInfo/Ext/Excelfore/Campaigns/2/CampaignEnd"]=V

## ECU NO1  ##############################################################################################################
node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/PkgURL"]=http://192.168.1.118/testdata/ecu-v1-enc.zip
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/PkgURL"]=chr
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/PkgURL"]=V

node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadLen"]=0
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadLen"]=int
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadLen"]=V

node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Length"]=2986
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Length"]=int
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Length"]=V

node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/EncryptionKey"]=MTIzNDU2Nzg5MDEyMzQ1Ng==
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/EncryptionKey"]=bin
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/EncryptionKey"]=V

node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/EncryptionMethod"]=AES/CTR/NoPadding
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/EncryptionMethod"]=chr
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/EncryptionMethod"]=V

node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Sha256"]=HyFuH/xKxYQAHB4O2J318TzjQkdyP/WKTwtRcxj8C7o=
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Sha256"]=chr
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Sha256"]=V

node_value["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Correlator"]=11
node_types["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Correlator"]=int
node_flags["FUMO/7905071-DB01-0x0011/Ext/Versions/vlibv1/DownloadAndUpdate/Correlator"]=V

## ECU NO2  ##############################################################################################################
node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/PkgURL"]=http://192.168.1.118/testdata/ecu-v2-enc.zip
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/PkgURL"]=chr
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/PkgURL"]=V

node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadLen"]=0
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadLen"]=int
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadLen"]=V

node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Length"]=4003
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Length"]=int
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Length"]=V

node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/EncryptionKey"]=MTIzNDU2Nzg5MDEyMzQ1Ng==
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/EncryptionKey"]=bin
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/EncryptionKey"]=V

node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/EncryptionMethod"]=AES/CTR/NoPadding
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/EncryptionMethod"]=chr
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/EncryptionMethod"]=V

node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Sha256"]=9Nqw7Xfq0rut4NIWATNVUUa08mVEqDO444TYMrbO+Fc=
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Sha256"]=chr
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Sha256"]=V

node_value["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Correlator"]=12
node_types["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Correlator"]=int
node_flags["FUMO/7905072-DB02-0x0012/Ext/Versions/vlibv2/DownloadAndUpdate/Correlator"]=V

## ECU NO3  ##############################################################################################################
node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/PkgURL"]=http://192.168.1.118/testdata/ecu-v3-enc.zip
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/PkgURL"]=chr
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/PkgURL"]=V

node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadLen"]=0
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadLen"]=int
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadLen"]=V

node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Length"]=5016
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Length"]=int
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Length"]=V

node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/EncryptionKey"]=MTIzNDU2Nzg5MDEyMzQ1Ng==
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/EncryptionKey"]=bin
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/EncryptionKey"]=V

node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/EncryptionMethod"]=AES/CTR/NoPadding
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/EncryptionMethod"]=chr
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/EncryptionMethod"]=V

node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Sha256"]=3AN1itCnqOSpFQtkR8xDQT/jOSms7iHYNL+gI/N0Hhw=
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Sha256"]=chr
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Sha256"]=V

node_value["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Correlator"]=13
node_types["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Correlator"]=int
node_flags["FUMO/7905073-DB03-0x0013/Ext/Versions/vlibv3/DownloadAndUpdate/Correlator"]=V





if [ ${#node_value[@]} -ne ${#node_types[@]} ]; then
	echo "error: node types don't match node values"
	exit
fi


DM_SERVER=/home/tiankang/Downloads/data/dmserver
DM_TREE=/home/tiankang/Downloads/data/dm_tree/

function setup_dmtree() {
	for key in ${!node_value[*]}
	do
		${DM_SERVER} -t ${DM_TREE} -P ${key} -T ${node_types[${key}]} -N ${node_flags[${key}]} -V ${node_value[${key}]}
	done
}


init()
{

	export ESYNC_HOME_DIR=/home/tiankang/Downloads/Excelforepackage/excelfore/esync
	export ESYNC_DATA_DIR=/fota-evo
	export ESYNC_DOWNLOAD_DIR=/fota-evo/download
	export ESYNC_LOG_DIR=/otalog-evo
	export LD_LIBRARY_PATH=$ESYNC_HOME_DIR/lib:$LD_LIBRARY_PATH
	export PATH=$ESYNC_HOME_DIR/bin:$ESYNC_HOME_DIR/xbin:$PATH

	mkdir -p $ESYNC_LOG_DIR/rotation
	mkdir -p $ESYNC_DOWNLOAD_DIR
}

function usage() {
	echo "Usage: $0 [-t dmtree -b dmserver]"
	echo "	-h show help"
	echo "	-t dmtree path"
	echo "	-b dmserver binary path"
	exit 1;
}

while getopts 'ht:b:' o; do
	case "${o}" in
		t)
			DM_TREE=${OPTARG}
			if [ ! -d ${DM_TREE} ]; then

				mkdir -p ${DM_TREE}
			fi
			;;
		b)
			DM_SERVER=${OPTARG}
			;;
		h)
			usage
			;;
		?)
			usage
			;;
	esac
done

if [ ! -f ${DM_SERVER} ]; then
	echo "error: dmsever not found dmserver=${DM_SERVER}"
	usage
fi

echo "dmtree=${DM_TREE}"
echo "dmserver=${DM_SERVER}"


init
setup_dmtree
