import os
from Messages.administration  import notify_admins, authentificate, check_serial_aviability
from config import serial_initialized
from data import users
from serial_talker import serial_talker
from webcam import shooter

telegramBot = [None, ]

def set_bot(new_bot):
    telegramBot[0] = new_bot
    print("Bot inited")

@notify_admins
def time(message):
    print(telegramBot[0])
    import time
    chat_id = message.chat_info.id
    text = str(time.time())
    telegramBot[0].sendMessage(chat_id, text)

@notify_admins    
def my_name(message):
    chat_id = message.chat_info.id    
    text = os.name
    telegramBot[0].sendMessage(chat_id, text)

@check_serial_aviability
@notify_admins    
def temperature(message):
    chat_id = message.chat_info.id
    degrees = serial_talker.execute_command('t')
    #degrees = 36.6
    text = "Temperature is {}".format(degrees)
    telegramBot[0].sendMessage(chat_id, text)

@authentificate
@notify_admins
def room_photo(message):
    pic_path = shooter.take_picture()
    # text notification
    chat_id = message.chat_info.id
    text = "Picture taken. Here you go:"
    telegramBot[0].sendMessage(chat_id, text)
    # send file
    with open(pic_path, 'rb') as photo:
        telegramBot[0].sendPhoto(chat_id, photo)
    

@authentificate
@notify_admins
def subscribe_to_notifications(message):
    chat_id = message.chat_info.id
    users.add_subscriber(message.from_info.username, chat_id)
    text = "Subscribed"
    telegramBot[0].sendMessage(chat_id, text)
    
def default_answer(message):
    chat_id = message.chat_info.id
    text = "I read you {}. No callback found for {}".format(message.from_info.username,  str(message.text))
    telegramBot[0].sendMessage(chat_id, text,
                    parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None)    

def custom_answer(chat_id, text):
    print (text)
    telegramBot[0].sendMessage(chat_id, text)                   

callbacks = {
            "/time" : time,
            "/myname" : my_name,
            "/temperature" : temperature,
            "/webcam" : room_photo,
            "/subscribe" : subscribe_to_notifications,
            }
    
