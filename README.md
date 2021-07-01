# hslu-pren-32

## Run
pi@raspberrypi:~/hslu-pren-32 $ `./run_app.sh`

## Installation (OS, WLAN, SSH)
- Use PI Imager https://www.raspberrypi.org/software/ to install latest OS

- Create wpa_supplicant.conf file on sd card
 
- Enter WiFi settings into new file:

```
country=CH
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="100GHz 5G Testing Antenna"
    psk="XXXXXXXXXXX"
    key_mgmt=WPA-PSK
}
```
- create file `ssh` so sd card

>ssh pi@192.168.x.x

default password is `raspberry`

change password of user pi with `passwd` to rpPREN32

## Setup VSCode
- Install recomendended extensions locally. Type `@recommended` in extensions search bar.
- Add new SSH Target in Remote Explorer and use `ssh pi@192.168.x.x`
- Connect to in new Window and log in with `rpPREN32`

## Install Software
 pi@raspberrypi:~ $ `git clone https://github.com/jonas99y/hslu-pren-32.git`

 pi@raspberrypi:~ $ `sudo chmod +x ./hslu-pren-32/install.sh`

 pi@raspberrypi:~ $ `./hslu-pren-32/install.sh`


