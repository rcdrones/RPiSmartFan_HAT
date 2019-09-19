#!/bin/bash

if [ $(id -u) -ne 0 ]; then #使用root权限
  printf "Script must be run as root. Try 'sudo xxx'\n"
  exit 1
fi

systemctl stop SmartFans_daemon
systemctl disable SmartFans_daemon


rm /home/pi/SmartFan.conf
rm /etc/systemd/system/SmartFans_daemon.service
rm /usr/sbin/SmartFans_daemon.py
rm /usr/sbin/rpi_info.py
rm /usr/sbin/sf
rm /usr/sbin/rpi.png





