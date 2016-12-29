import os
import config
import telepot
from pprint import pprint

from Messages import messages, palette

def message_callback(new_messages):
    print("______________new message!____________")
    #print(new_messages)
    parser = messages.MessagePasrser()
    parsed_messages = parser.parse(new_messages)
    for message in parsed_messages:
        print ("from: {}{}Message: {}".format( message.from_info.username, os.linesep, message.text))
        callback = palette.callbacks.get(message.text, palette.default_answer)
        callback(TelegramBot, message)
    
    
# Create bot instance with token
TelegramBot = telepot.Bot(config.BOT_TOKEN)
# Run bot loop
# relax param is seconds between each call to telegram serv
TelegramBot.message_loop(message_callback, 
                         relax=config.server_query_frequency, 
                         timeout=20, 
                         ordered=True, 
                         maxhold=3, 
                         run_forever=True
                         )


# test ground
#message_callback(messages.dict_message_example)
