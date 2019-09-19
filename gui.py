#!/usr/bin/python3


import tkinter as tk
import json

def_config = {"speed":1, "threshold":50}
cfg_speed = 0
cfg_threshold = 0

def pre_fetch_cfg():
    global cfg_speed, cfg_threshold
    try:
        with open("/home/pi/SmartFan.conf","r") as f_cfg:
            f = f_cfg.read()
    except:
        with open("/home/pi/SmartFan.conf","w") as f_cfg:
            json.dump(def_config,f_cfg,indent=4)

        with open("/home/pi/SmartFan.conf","r") as f_cfg:
            f = f_cfg.read()

    config = json.loads(f)
    #print(config)
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
    with open("/home/pi/SmartFan.conf","w") as f_cfg:
        json.dump(def_config,f_cfg,indent=4)

    l_temp.config(text='CPUTemp : ' + v + " Celsius")
    
    

# scale bar
s_temp = tk.Scale(window, label='Fan ON/OFF threshold:', from_=30, to=80, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=10, resolution=1, command=cpu_temp)
s_temp.set(cfg_threshold)
s_temp.place(x=10,y=280,anchor="nw")




#------------------------------------


# label
l_speed = tk.Label(window, bg='yellow', width=25, text='')
l_speed.place(x=200,y=360,anchor="nw")


def fan_speed():
    global def_config
    def_config["speed"] = int(r.get())
    with open("/home/pi/SmartFan.conf","w") as f_cfg:
        json.dump(def_config,f_cfg,indent=4)
    
    if r.get() == 1 :
        l_speed.config(text='Fans Mode : Quiet')
    elif r.get() == 2 :
        l_speed.config(text='Fans Mode : Performance')


r = tk.IntVar()
quit_select = tk.Radiobutton(window,text='Quiet Mode',value=1,variable=r,command=fan_speed)
quit_select.place(x=30,y=345,anchor="nw")
pfm_select = tk.Radiobutton(window,text='Performance Mode',value=2,variable=r,command=fan_speed)
pfm_select.place(x=30,y=370,anchor="nw")




#s_speed = tk.Scale(window, label='Fan Speed:', from_=30, to=100, orient=tk.HORIZONTAL,
#             length=200, showvalue=0, tickinterval=10, resolution=1, command=fan_speed)
#s_speed.set(cfg_speed)
#s_speed.place(x=10,y=340,anchor="nw")


window.mainloop()

