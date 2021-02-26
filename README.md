# hslu-pren-32

## Installation
- Use PI Imager https://www.raspberrypi.org/software/ to install latest OS

- Create wpa_supplicant.conf file on sd card
 
- Enter WiFi settings into new file:

```
country=CH
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="100GHz 5G Testing Antenna"
    psk="70794440629274328194"
    key_mgmt=WPA-PSK
}
```
- create file `ssh` so sd card

>ssh pi@192.168.x.x

password is raspberry



