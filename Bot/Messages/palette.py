

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
    degrees = 36.6
    text = "Temperature is {}c".format(degrees)
    bot.sendMessage(chat_id, text)

callbacks = {
            "/time" : time,
            "/myName" : my_name,
            "/temperature" : temperature,
            }