#!/usr/bin/sh
echo "Packages installation: "
apt-get install gcc g++ git python3 python3-pip sshpass gedit curl
echo "Dependencies installation: "
python3 -m pip install -r requirements.txt
