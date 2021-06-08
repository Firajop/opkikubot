#!/usr/bin/env bash
# opkikubot - UserBot
# Copyright (C) 2020 opkikubot
#
# This file is a part of < https://github.com/opgohil/opkikubot/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/opgohil/opkikubot/blob/main/LICENSE/>.

clear
echo -e "\e[1m"
echo "    ____        _    _ _          _           _   
  / __ \      | |  (_) |        | |         | |  
 | |  | |_ __ | | ___| | ___   _| |__   ___ | |_ 
 | |  | | '_ \| |/ / | |/ / | | | '_ \ / _ \| __|
 | |__| | |_) |   <| |   <| |_| | |_) | (_) | |_ 
  \____/| .__/|_|\_\_|_|\_\\__,_|_.__/ \___/ \__|
        | |                                      
        |_|                                       "
echo "  "
echo "  "
echo "  "
echo "  "
echo "  "
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/opgohil/opkikubot/main/resources/session/ssgen.py
pip install telethon
clear
python3 ssgen.py
