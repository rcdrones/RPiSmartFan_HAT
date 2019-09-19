#!/bin/bash

if [ $(id -u) -ne 0 ]; then #使用root权限
  printf "Script must be run as root. Try 'sudo xxx'\n"
  exit 1
fi


echo "dtoverlay=pi3-miniuart-bt" | sudo tee -a /boot/config.txt &> /dev/null

echo "enable_uart=1" | sudo tee -a /boot/config.txt &> /dev/null

echo "dtoverlay=gpio-shutdown,gpio_pin=4,active_low=1" | sudo tee -a /boot/config.txt &> /dev/null


wget -O /etc/systemd/system/SmartFans_daemon.service https://github.com/rcdrones/RPiSmartFan_HAT/raw/master/SmartFans_daemon.service

wget -O /usr/sbin/SmartFans_daemon.py https://github.com/rcdrones/RPiSmartFan_HAT/raw/master/SmartFans_daemon.py

wget -O /usr/sbin/rpi_info.py https://github.com/rcdrones/RPiSmartFan_HAT/raw/master/rpi_info.py

wget -O /usr/sbin/sf https://github.com/rcdrones/RPiSmartFan_HAT/raw/master/gui.py

wget -O /usr/sbin/rpi.png https://github.com/rcdrones/RPiSmartFan_HAT/raw/master/rpi.png


chmod 777 /etc/systemd/system/SmartFans_daemon.service
chmod 777 /usr/sbin/SmartFans_daemon.py
chmod 777 /usr/sbin/rpi_info.py
chmod 777 /usr/sbin/sf

chown root:root /etc/systemd/system/SmartFans_daemon.service
chown root:root /usr/sbin/SmartFans_daemon.py
chown root:root /usr/sbin/rpi_info.py


systemctl enable SmartFans_daemon
systemctl start SmartFans_daemon &

reboot
