import os
import config
import threading
import telepot

import lanscan
import bluetooth
from Messages import palette
from serial_talker import serial_talker
    
def launch_bot_thread():
    # Create bot instance with token
    TelegramBot = telepot.Bot(config.BOT_TOKEN)
    palette.set_bot(TelegramBot)
    # Run bot loop
    TelegramBot.message_loop(palette.message_callback, 
                             relax=config.server_query_frequency,     
                             # relax param is seconds between each call to telegram serv
                             timeout=120, 
                             ordered=True, 
                             maxhold=3, 
                             run_forever=True
                             )

from events import HomeEventHandler # don't move this import up
event_handler = HomeEventHandler()
#lanscan.run_lanscan_loop(event_handler)                             
bluetooth.run_worker(event_handler)
serial_talker.set_event_handler(event_handler)
#serial_talker.run_serial_mocker()
launch_bot_thread()





