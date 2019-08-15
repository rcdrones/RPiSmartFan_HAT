#!/usr/bin/python3


import tkinter as tk
import json

def_config = {"speed":100, "threshold":50}
cfg_speed = 0
cfg_threshold = 0

def pre_fetch_cfg():
    global cfg_speed, cfg_threshold
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

pre_fetch_cfg()
window = tk.Tk()
window.title("RPi Smart Fan HAT")
window.geometry("400x400")

#tk.Label(window,text="1111").pack()


canvas = tk.Canvas(window, width=400,height=268)

image_file = tk.PhotoImage(file='rpi.png')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack()



#tk.Label(window,text="Fan ON/OFF Threshold").place(x=20,y=280,anchor="nw")

#orcodinate

l_temp = tk.Label(window, bg='yellow', width=20, text='')
l_temp.place(x=220,y=300,anchor="nw")

def cpu_temp(v):
    global def_config
    def_config["threshold"] = int(v)
    with open("/home/pi/SmartFan.cfg","w") as f_cfg:
        json.dump(def_config,f_cfg,indent=4)

    l_temp.config(text='CPUTemp : ' + v + " Celsius")

s_temp = tk.Scale(window, label='Fan ON/OFF threshold:', from_=40, to=80, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=10, resolution=1, command=cpu_temp)
s_temp.set(cfg_threshold)
s_temp.place(x=10,y=280,anchor="nw")


l_speed = tk.Label(window, bg='yellow', width=20, text='')
l_speed.place(x=220,y=360,anchor="nw")

def fan_speed(v):
    global def_config
    def_config["speed"] = int(v)
    with open("/home/pi/SmartFan.cfg","w") as f_cfg:
        json.dump(def_config,f_cfg,indent=4)

    l_speed.config(text='Fan Speed : ' + v +"%")

s_speed = tk.Scale(window, label='Fan Speed:', from_=30, to=100, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=10, resolution=1, command=fan_speed)
s_speed.set(cfg_speed)
s_speed.place(x=10,y=340,anchor="nw")


window.mainloop()

