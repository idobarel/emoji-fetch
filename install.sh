#!/bin/sh
wget https://raw.githubusercontent.com/idobarel/emoji-fatch/main/main.py
mv main.py ef
chmod +x ef
sudo mv ef /usr/local/bin
clear
echo "Done! Use ef"
