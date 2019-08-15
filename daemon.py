#!/usr/bin/python3

import rpi_info
import time
import serial
import os,sys
import json

ser = serial.Serial("/dev/ttyAMA0", 9600)

if ser != None:
    print("serial0 init ok.")
else:
    print("config serial0 first!")

pi4 = rpi_info.RPI_INFO()

cpu = 0
mem = 0
tmp = 0

cfg_speed = 100
cfg_threshold = 50

def get_info():
    global cpu, mem, tmp
    pi4.get_all()

    cpu = pi4.cpu_usage
    mem = pi4.memory_usage
    tmp = pi4.cpu_temp

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value    #Instance of str

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value    #Instance of bytes

def get_cfg():
    global cfg_speed, cfg_threshold

    def_config = {"speed":100, "threshold":50}

    try:
        with open("/home/pi/SmartFan.cfg","r") as f_cfg:
            f = f_cfg.read()
    except:
        with open("/home/pi/SmartFan.cfg","w") as f_cfg:
            json.dump(def_config,f_cfg,indent=4)

        with open("/home/pi/SmartFan.cfg","r") as f_cfg:
            f = f_cfg.read()

    config = json.loads(f)
    print(config)
    for x,y in config.items():
        if x == "speed" :
            cfg_speed = y
        elif x == "threshold" :
            cfg_threshold = y


def send_buf():
    global cfg_speed, cfg_threshold
    get_cfg()
    send_buf = ""
    get_info()
    #print(cpu,mem,tmp)

    if tmp >= cfg_threshold:
        speed_tmp = cfg_speed
    else:
        speed_tmp = 0

    send_buf = "$SmartFAN,"+str(cpu)+","+str(mem)+","+str(speed_tmp)+","+str((cpu+mem+speed_tmp)%100)+"$"
    #print(send_buf)
    send_buf = to_bytes(send_buf)
    print(send_buf)
    ser.write(send_buf)
    time.sleep(1)

def recv_proc():
     data = ''
     data = data.encode('utf-8')
     time.sleep(0.1)
     n = ser.inWaiting()
     if n:
         data = data + ser.read(n)
         print('get data from serial port:', data)
         #print(type(data))

         str_tmp = to_str(data).strip("")
         str_tmp = to_str(data).strip("$")

         print(str_tmp)

         recv_buf = str_tmp.split(",")

         #print(recv_buf)

         fan_speed = int(recv_buf[1])
         halt_reboot = int(recv_buf[2])
         check_sum = int(recv_buf[3])


         if (fan_speed+halt_reboot)%100 == check_sum :
             #print("recv ok")
             if halt_reboot == 0:
                 #print("0.normal op,send back ")
                 send_buf()
             elif halt_reboot == 1:
                 print("1.halt")
                 #os.system("sudo halt")
             elif halt_reboot== 2:
                 print("2.reboot")
                 #os.system("sudo reboot")
         else:
             print("check_sum error!")

def main():
    while True:
        try:
            recv_proc()
        except:
            continue





if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        if ser != None:
            ser.close()