import config
import telepot
from pprint import pprint

from Messages import messages   



def message_callback(new_messages):
    print("new message!")
    #print(new_messages)
    parser = messages.MessagePasrser()
    parsed_messages = parser.parse(new_messages)
    for message in parsed_messages:
        echo(message)
    
def echo(message):
    chat_id = message.chat_info.id
    text = "I read you " + \
           message.from_info.username + \
           " " + \
           str(message.date)
    TelegramBot.sendMessage(chat_id, text,
                    parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None)

    
    
TelegramBot = telepot.Bot(config.BOT_TOKEN)
message_callback(TelegramBot.getUpdates())




TelegramBot.message_loop(message_callback, relax=1, timeout=20, ordered=True, maxhold=3, run_forever=True)