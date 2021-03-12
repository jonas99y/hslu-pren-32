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
eval cd ..
eval apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev
eval cd Python-3.9.2
eval ./configure
eval make
eval make install
eval cd ..
eval pip3 install -r hslu-pren-32/src/requirements.txt

eval curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
eval sudo apt install nodejs
eval sudo npm install -g @angular/cli
eval cd oivonen-web
eval npm install
eval cd ..
eval chmod +x ./hslu-pren-32/run.sh
eval chmod +x ./hslu-pren-32/run_web.sh
eval chmod +x ./hslu-pren-32/run_remote_server.sh
eval apt install parallel
