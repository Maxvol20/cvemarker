#!usr/bin/sh
echo "Packages installation: "
apt-get install gcc g++ git python3 sshpass gedit
echo "Dependencies installation: "
python3 -m pip install -r requirements.txt
