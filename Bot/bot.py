import os
import config
import threading
import telepot

import lanscan
from Messages import palette
    
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
lanscan.run_lanscan_loop(event_handler)                             
launch_bot_thread()



