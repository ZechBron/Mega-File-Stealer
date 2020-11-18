#!/bin/bash

update() {
   cd $HOME
   rm -rf Mega-File-Stealer
   git clone https://github.com/ZechBron/Mega-File-Stealer
}

if [ "$zCh" = "Version 2.0" ]; then
echo -e "\e[92mNo latest update\e[0m"

elif [ "$zCh" = "Version 2.1" ]; then
update
echo -e " \e[92mUpdate done\e[0m"

elif [ "$zCh" = "Version 2.2" ]; then
update
echo -e "\e[92mUpdate done\e[0m"
fi
