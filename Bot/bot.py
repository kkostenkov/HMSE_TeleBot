import os
import config
import threading
import telepot


import lanscan
from Messages import messages, palette

def message_callback(new_messages):
    print("______________new message!____________")
    #print(new_messages)
    parser = messages.MessagePasrser()
    parsed_messages = parser.parse(new_messages)
    for message in parsed_messages:
        print ("from: {}{}Message: {}".format( message.from_info.username, os.linesep, message.text))
        callback = palette.callbacks.get(message.text, palette.default_answer)
        callback(message)
    
def launch_bot_thread():
    # Create bot instance with token
    TelegramBot = telepot.Bot(config.BOT_TOKEN)
    palette.set_bot(TelegramBot)
    # Run bot loop
    # relax param is seconds between each call to telegram serv
    TelegramBot.message_loop(message_callback, 
                             relax=config.server_query_frequency, 
                             timeout=120, 
                             ordered=True, 
                             maxhold=3, 
                             run_forever=True
                             )

from events import HomeEventHandler # don't move this import up
event_handler = HomeEventHandler()
lanscan.run_lanscan_loop(event_handler)                             
launch_bot_thread()



