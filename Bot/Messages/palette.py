from config import serial_initialized
from serial_talker import serial_talker
from webcam import shooter

NO_SERIAL_NOTIFICATION = "No connection through serial port. =("

def time(bot, message):
    import time
    chat_id = message.chat_info.id
    text = str(time.time())
    bot.sendMessage(chat_id, text)
    
def my_name(bot, message):
    chat_id = message.chat_info.id
    import os, sys
    text = os.name + " " + sys.winver
    bot.sendMessage(chat_id, text)
    
def temperature(bot, message):
    chat_id = message.chat_info.id
    if not serial_initialized:
        bot.sendMessage(chat_id, NO_SERIAL_NOTIFICATION)
        return
    degrees = serial_talker.execute_command('t')
    #degrees = 36.6
    text = "Temperature is {}".format(degrees)
    bot.sendMessage(chat_id, text)

def room_photo(bot, message):
    pic_path = shooter.take_picture()
    # text notification
    chat_id = message.chat_info.id
    text = "Picture taken. Here you go:"
    bot.sendMessage(chat_id, text)
    # send file
    with open(pic_path, 'rb') as photo:
        bot.sendPhoto(chat_id, photo)
    

    

callbacks = {
            "/time" : time,
            "/myName" : my_name,
            "/temperature" : temperature,
            "/webcam" : room_photo,
            }
    
