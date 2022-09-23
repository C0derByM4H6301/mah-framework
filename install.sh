#!/bin/bash
echo "Installation started!!!"
chmod +x mah-framework.py 
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo apt-get install tor -y
sudo pip3 install colorama
sudo pip3 install os
sudo pip3 install time
sudo pip3 install argparse
sudo pip3 install logging
sudo pip3 install readline
sudo pip3 install pyfiglet
sudo pip3 install progressbar
sudo pip3 install emoji
sudo pip3 install distutils
sudo pip3 install py2exe
sudo pip3 install termcolor
sudo pip3 install -r modules/Anominy/torghost/requirements.txt
sudo chmod 777 modules/Anominy/torghost/torghost.py
bash modules/Anominy/torghost/build.sh
sudo rm -rf build
echo "installation successful!"
