#!usr/bin/sh
echo "Packages installation: "
apt-get install gcc g++ git python2.7 python3 sshpass
apt-get install gcc g++ git python2.7 python3 sshpass gedit
echo "Setting Python2.7 as default for installing dependencies."
update-alternatives --install /usr/bin/python python /usr/bin/python3 1
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 10
echo "Installing PIP: "
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo "Dependencies installation: "
python -m pip install -r requirements.txt
echo "Setting Python3 as default."
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3 10
