#!/bin/sh
wget https://raw.githubusercontent.com/idobarel/emoji-fatch/main/main.py
wget https://raw.githubusercontent.com/idobarel/emoji-fatch/main/requirements.txt
sudo apt-get install dos2unix
pip3 install -r requirements.txt
mv main.py ef
dos2unix ef
chmod +x ef
sudo mv ef /usr/local/bin
rm requirements.txt
clear
echo "Done! Use ef"
