#!/bin/sh
wget https://raw.githubusercontent.com/idobarel/stock-fetch/main/main.py
wget https://raw.githubusercontent.com/idobarel/stock-fetch/main/requirements.txt
sudo apt-get install dos2unix
pip3 install -r requirements.txt
mv main.py sf
dos2unix sf
chmod +x sf
sudo mv ef /usr/local/bin
rm requirements.txt
clear
echo "Done! Use sf [stock | crypto]"