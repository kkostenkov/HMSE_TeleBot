import os
from Messages.administration  import notify_admins, authentificate
from config import serial_initialized
from serial_talker import serial_talker
from webcam import shooter

NO_SERIAL_NOTIFICATION = "No connection through serial port. =("

@notify_admins
def time(bot, message):
    import time
    chat_id = message.chat_info.id
    text = str(time.time())
    bot.sendMessage(chat_id, text)

@notify_admins    
def my_name(bot, message):
    chat_id = message.chat_info.id    
    text = os.name
    bot.sendMessage(chat_id, text)

@notify_admins    
def temperature(bot, message):
    chat_id = message.chat_info.id
    if not serial_initialized:
        bot.sendMessage(chat_id, NO_SERIAL_NOTIFICATION)
        return
    degrees = serial_talker.execute_command('t')
    #degrees = 36.6
    text = "Temperature is {}".format(degrees)
    bot.sendMessage(chat_id, text)

@authentificate
@notify_admins
def room_photo(bot, message):
    pic_path = shooter.take_picture()
    # text notification
    chat_id = message.chat_info.id
    text = "Picture taken. Here you go:"
    bot.sendMessage(chat_id, text)
    # send file
    with open(pic_path, 'rb') as photo:
        bot.sendPhoto(chat_id, photo)
    

def default_answer(bot, message):
    chat_id = message.chat_info.id
    text = "I read you {}. No callback found for {}".format(message.from_info.username,  str(message.text))
    bot.sendMessage(chat_id, text,
                    parse_mode=None, disable_web_page_preview=None,
                    disable_notification=None, reply_to_message_id=None, reply_markup=None)    

def non_authorized_answer(bot, message):
    chat_id = message.chat_info.id
    text = "%s, you're not permitted to execute this command." % message.from_info.username
    print (text)
    bot.sendMessage(chat_id, text)                   

callbacks = {
            "/time" : time,
            "/myName" : my_name,
            "/temperature" : temperature,
            "/webcam" : room_photo,
            }
    
