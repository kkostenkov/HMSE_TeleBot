# -*- coding: utf-8 -*-
import os

# Telegram
BOT_TOKEN = "122834554:AAGhslxsCbB63iGrEWwCqGA9IhbVxrRcnto"
server_query_frequency = 60 # in seconds

serial_initialized = False

admins = [ "kiparis87", ]

# Wi-Fi
ips_to_scan = ["192.168.100." + str(a) for a in range(11)]
wifi_scan_frequency = 180 # once every %scan_frequency% seconds 
known_macs = { 
                  ("38", "a4", "ed", "05", "bd", "02") : "kirill",
                  ("f8", "27", "93", "30", "5a", "ca") : "vika",
                  }

# Bluetoth
max_offline_time = 60 * 60 * 5  # seconds
bt_rollcall_freq = 30 * 60 # seconds
known_bt_devices = {
        "kirill": "74:23:44:A3:24:4E", 
        "vika": "D0:81:7A:40:A4:C4",
        }

def get_serial_port():
    if (os.name == "nt"):
        port = "COM3"
    else:
        port = "/dev/ttyACM0"
    return port


# audio
mp3_player = "mpg321"
wav_player = "play"
