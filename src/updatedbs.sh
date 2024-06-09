#!/bin/bash
trap ' ' 2 20

spinerFunction(){
    local i sp n
    chars="/-\|"
    n=${#chars}
    printf ' '
    while sleep 0.1; do
        printf "%s\b" "${chars:i++%n:1}"
    done
}
sudo openvpn "$1" &> /dev/null &
firstLine="$(head -1 $2)"
if [ ! -d .temcsv/ ];then
    mkdir .temcsv
    cd .temcsv/
    touch .tem
else
    cd .temcsv/
    touch .tem
fi
tail -n +2 "$2">.tem
sed -i 's/\"//g' .tem
IFC=""
while read i; do
    tt="$(cut -d "," -f 1 <<<"$i")"
    ipsrc="$(cut -d "," -f 2 <<<"$i")"
    ipdst="$(cut -d "," -f 3 <<<"$i")"
    protocol="$(cut -d "," -f 4 <<<"$i")"
    length="$(cut -d "," -f 5 <<<"$i")"
    info="$(cut -d "," -f 6 <<<"$i")"
    printf "\n"
    printf "Saving remote data "
    spinerFunction &
    sleep 3
    kill "$!"
    ssh "$3@$4" << EOF
    mariadb -u root -proot ids -e "INSERT INTO traffic (time, ipsrc, ipdst, protocol, packlen, info) VALUES ($tt, '$ipsrc', '$ipdst', '$protocol', $length, '$info')"

EOF
done<.tem
echo "Saved Data returning to main menu..."
rm -rf .temcsv
cd ../..
echo "Exit from VPN..."
pkill openvpn
sleep 3
clear
trap - 2 20