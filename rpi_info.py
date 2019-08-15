#!/usr/bin/python3

import psutil

class RPI_INFO():

    def __init__(self):
        self.cpu_usage = 1
        self.memory_usage = 1
        self.cpu_temp = 25


    def get_all(self):
        cpu = psutil.cpu_percent(interval = 1)
        #print(cpu)
        self.cpu_usage = int(cpu)

        memory = psutil.virtual_memory()
        memory_usage = float(memory.used) / float(memory.total)
        self.memory_usage = int(memory_usage*100)

        temps = psutil.sensors_temperatures()
        for name, entries in temps.items():
            for entry in entries:
                self.cpu_temp = int(entry.current)
                #print("  %s °C " %  str(int(entry.current)))

    def get_cpu_usage(self):
        cpu = psutil.cpu_percent()
        self.cpu_usage = int(cpu)

