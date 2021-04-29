eval echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
eval curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
eval sudo apt update
eval sudo apt upgrade
eval sudo apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev
eval pip3 install -r hslu-pren-32/src/requirements.txt

eval sudo apt install python3-tflite-runtime

eval chmod +x hslu-pren-32/run.sh
eval chmod +x hslu-pren-32/run_web.sh
eval chmod +x hslu-pren-32/run_remote_server.sh
eval chmod +x hslu-pren-32/install-rdp.sh
eval chmod +x hslu-pren-32/install-web.sh

eval sudo raspi-config nonint do_camera 0
eval echo "Pleas reboot with 'sudo reboot'"
