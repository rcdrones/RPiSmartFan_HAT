#!/bin/bash

if [ $(id -u) -ne 0 ]; then #使用root权限
  printf "Script must be run as root. Try 'sudo xxx'\n"
  exit 1
fi


echo "### add by Smartfan hat ####" | sudo tee -a /boot/config.txt &> /dev/null

echo "dtoverlay=pi3-miniuart-bt" | sudo tee -a /boot/config.txt &> /dev/null

echo "enable_uart=1" | sudo tee -a /boot/config.txt &> /dev/null

echo "dtoverlay=gpio-shutdown,gpio_pin=4,active_low=1" | sudo tee -a /boot/config.txt &> /dev/null


