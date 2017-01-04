# -*- coding: utf-8 -*-
import os

BOT_TOKEN = "122834554:AAGhslxsCbB63iGrEWwCqGA9IhbVxrRcnto"
server_query_frequency = 10 # in seconds

serial_initialized = False

admins = [ "kiparis87", ]

ips_to_scan = ["192.168.100." + str(a) for a in range(15)]
wifi_scan_frequency = 60 # once every %scan_frequency% seconds 

def get_serial_port():
    if (os.name == "nt"):
        port = "COM3"
    else:
        port = "/dev/ttyACM0"
    return port
