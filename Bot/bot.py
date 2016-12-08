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
        
        callback = palette.callbacks.get(message.text, default_answer)
        callback(TelegramBot, message)
    
def default_answer(bot, message):
    chat_id = message.chat_info.id
    text = "I read you {}. No callback found for {}".format(message.from_info.username,  str(message.text))
    bot.sendMessage(chat_id, text,
                    parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None)

    
# Create bot instance with token
TelegramBot = telepot.Bot(config.BOT_TOKEN)
# Run bot loop
TelegramBot.message_loop(message_callback, relax=1, timeout=20, ordered=True, maxhold=3, run_forever=True)


# test ground
#message_callback(messages.dict_message_example)