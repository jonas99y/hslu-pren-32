eval apt update
eval apt upgrade
eval wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz
eval tar xf Python-3.9.2.tar.xz
eval cd Python-3.9.2
eval configure
eval make -j -l 4
eval sudo make altinstall
eval echo "alias python3=python3.9" >> ~/.bashrc
eval echo "alias pip3=pip3.9" >> ~/.bashrc
eval source ~/.bashrc