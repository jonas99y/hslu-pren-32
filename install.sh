eval echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
eval curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
eval apt update
eval apt upgrade
eval apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev


# eval wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tar.xz
# eval tar xf Python-3.7.9.tar.xz
# eval cd Python-3.7.9
# eval ./configure
# eval make -j -l 4
# eval sudo make install
# eval echo "alias python3=python3.7" >> ~/.bashrc
# eval echo "alias pip3=pip3.7" >> ~/.bashrc
# eval source ~/.bashrc
# eval cd ..
eval pip3 install -r hslu-pren-32/src/requirements.txt

eval sudo apt install python3-tflite-runtime
# for the webapp:
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


eval raspi-config nonint do_camera 0
eval echo "Pleas reboot with 'sudo reboot'"
