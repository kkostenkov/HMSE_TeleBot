from serial_talker import serial_talker
from webcam import shooter

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
    photo=open(pic_path, 'rb')
    bot.sendPhoto(chat_id, photo)
    

    

callbacks = {
            "/time" : time,
            "/myName" : my_name,
            "/temperature" : temperature,
            "/webcam" : room_photo,
            }
    