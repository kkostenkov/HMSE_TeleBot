import os
from Messages.administration  import notify_admins, authentificate, check_serial_aviability
from Messages.messages import MessageParser

from config import serial_initialized
from data import users
from serial_talker import serial_talker
from speech import speech
from webcam import shooter

telegramBot = [None, ]

def set_bot(new_bot):
    telegramBot[0] = new_bot
    print("Bot inited")

@notify_admins
def time(message):
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
    degrees = serial_talker.execute_command("/t")
    text = "Temperature is {}".format(degrees)
    telegramBot[0].sendMessage(chat_id, text)

def test_audio(message):
    chat_id = message.chat_info.id
    text = "Testing speech module."
    telegramBot[0].sendMessage(chat_id, text)
    speech.ding()    
    
    
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
            "/myname" : my_name,
            "/temperature" : temperature,
            "/test_audio" : test_audio,
            "/time" : time,
            "/subscribe" : subscribe_to_notifications,
            "/webcam" : room_photo,
            }
    
def message_callback(new_messages):
    print("______________new message!____________")
    parser = MessageParser()
    parsed_messages = parser.parse(new_messages)
    for message in parsed_messages:
        print ("from: {}{}Message: {}".format( message.from_info.username, os.linesep, message.text))
        callback = callbacks.get(message.text, default_answer)
        callback(message)
