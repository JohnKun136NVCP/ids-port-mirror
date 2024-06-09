#!/bin/bash
trap ' ' 2 20
#colors
cyan='\033[0;36m'
lblue='\033[1;34m'
red='\033[0;31m'
function wiresharkFunction (){
  csvDataDirectory="csvdata"
  echo -e "${lblue}Make sure you all ready installed wireshark and tshark"
  read -p "Type name for wireshark catch file(without extensions): " wirefile
  sleep 0.5
  for _ in once; do
    if [ -d records/ ]
    then
        cd records/
        touch "$wirefile".pcap
        break
    else
        mkdir records
        cd records/
        touch "$wirefile".pcap
        break
    fi
  done
  echo "Showing interfaces for Wireshark. Choose your interface of network (WAN/LAN)"
  ifconfig -a
  read -p "Type the interface: " intNetwork
  clear
  echo -e "${red}WARNING!!\n Wireshark will execute soon\n when you finish your scanning, please save it as .csv file and quit id column"
  sleep 0.5
  for _ in once;do
    if [ -f "$csvDataDirectory" ]
    then
        echo -e "${lblue}Automatically, it will be created a directory (csvdata) if you want to save your files..."
        mkdir csvdata
        echo "Directory created"
        break
    else
        break
    fi
  done
  sleep 0.5
  tail -f -c 0 "$wirefile".pcap | wireshark -k -i "$intNetwork" -R "ip || ip.src == $1" -Y "ip || ip.src == $1" -w "$wirefile".pcap;
  echo "Data saved it"
}

function esp32Ids(){
    cd ../
    cd pyfiles/
    if [ ! -z "$1" ] && [ ! -z "$2" ]; then
        python3 esp32listener.py "$1" "$2"
    else
        echo "ERROR. MAKE SURE IF YOU ARE GIVING CORRECT PATH"
    fi
}

echo -e "${cyan} Welcome to IDS Mirrow, please check, you save  EPSP32's IP address on file."
file=$1
if [ ! -z "$file" ]
then
    echo "Getting ip..."
    sleep 0.5
    if [ -f "$file" ]
    then
        ip="$(cat $file)"
        wiresharkFunction $ip
        read -p "Path of your CSV saved: " csvSavedFile
        esp32Ids "$csvSavedFile" "$file"
        cd ..
    else
        echo "Your path or file doesn't exist"
        echo "First execute number 2 option from main.sh to get your IP"
        exit 1
    fi  
else
    echo "FILE EMPTY"
fi
trap - 2 20