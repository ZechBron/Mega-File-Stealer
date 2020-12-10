#!/bin/bash
zCh=$(curl https://raw.githubusercontent.com/ZechBron/Mega-File-Stealer/zMFS/update)

update() {
cd $HOME
rm -rf Mega-File-Stealer
git clone https://github.com/ZechBron/Mega-File-Stealer
}

if [ "$zCh" == "Version 2.3" ]; then
echo -e "\e[91mNo latest version available\e[0m"

elif [ "$zCh" == "Version 2.4" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 2.4\e[0m"

elif [ "$zCh" == "Version 2.5" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 2.5\e[0m"

elif [ "$zCh" == "Version 2.6" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 2.6\e[0m"

elif [ "$zCh" == "Version 2.7" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 2.7\e[0m"

elif [ "$zCh" == "Version 2.8" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 2.8\e[0m"

elif [ "$zCh" == "Version 2.9" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 2.9\e[0m"

elif [ "$zCh" == "Version 3.0" ]; then
update
echo -e "\e[92mMega File Stealer updated to Version 3.0\e[0m"
fi
