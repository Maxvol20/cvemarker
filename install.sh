#!usr/bin/sh
echo "Installing PIP: "
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo "Installing dependencies: "
pip install -r requirements.txt
