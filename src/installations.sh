#!/bin/bash
spinerFunction(){
    local i sp n
    chars="/-\|"
    n=${#chars}
    printf ' '
    while sleep 0.1; do
        printf "%s\b" "${chars:i++%n:1}"
    done
}


if PACKET="$( which apt-get )" 2> /dev/null;then
    #Debian packets
    echo "WARNING!! UBUNTU and derivates from version 23.10 doesn't work well..."
    sleep 0.5
    printf "Installing for debian packages"
    spinerFunction &
    sleep 5
    sudo add-apt-repository ppa:wireshark-dev/stable
    sudo apt-get update
    kill "$!"
    printf "Installing Wireshark"
    spinerFunction &
    sleep 5
    sleep 0.5
    sudo apt install wireshark-cli
    sudo apt install tshark
    kill "$!"
    echo "Select YES if any user's able to run wireshark without root permissions"
    echo "If it's necessary to reboot your computer, only run again the script"
    sleep 4
    echo "Packets installed"
    sleep 4
    clear
elif PACKET="$( which dnf )" 2> /dev/null; then
    #Redhat and fedora distros
    printf "Installing packages"
    spinerFunction &
    sleep 5
    sudo dnf install wireshark -y
    echo "If it's necessary to reboot your computer, only run again the script"
    sleep 4
    kill "$!"
    echo "Packets installed..."
    sleep 4
    printf "Giving permissions to /usr/bin/dumpcap"
    spinerFunction &
    sudo dpkg-reconfigure wireshark-common
    sudo chmod +x /usr/bin/dumpcap
    kill "$!"
    clear
elif PACKET="$( which emerge )" 2> /dev/null; then
    #Gentoo distros based
    printf "Installing Wireshark "
    spinerFunction &
    sleep 5
    sudo emerge --ask net-analyzer/wireshark
    kill "$!"
    printf "Hardware permissions "
    spinerFunction &
    sudo gpasswd -a ${LOGNAME} pcap
    sudo newgrp pcap
    kill "$!"
    echo "If you want to use Wireshark over SSH, please see https://wiki.gentoo.org/wiki/Wireshark \nFor more information..."
    sleep 4
    clear
elif PACKET="$( which pacman )" 2> /dev/null; then
    #Arch linux distros
    printf "Installing Wireshark..."
    spinerFunction &
    sleep 5
    sudo pacman -S wireshark-cli wireshark-gtk
    kill "$!"
    printf "Giving permissions to /usr/bin/dumpcap "
    spinerFunction &
    sudo chmod +x /usr/bin/dumpcap
    sleep 1
    kill "$!"
    clear
else
    echo "It was an error on installation..."
    sleep 2
    exit 1
fi 