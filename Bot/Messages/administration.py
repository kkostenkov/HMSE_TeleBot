import config
from data import users
import Messages.palette

def notify_admins(fn):
    def wrapped(message):
        sender = message.from_info.username
        action = message.text
        text = "%s asked for %s" % (sender, action)
        for admin, admin_chat_id in users.get_subscribers().items():
            Messages.palette.custom_answer(admin_chat_id, text)
        fn(message)
    return wrapped
    
def authentificate(fn):
    def wrapped(message):
        sender = message.from_info.username
        if sender in config.admins:
            fn(message)
        else:
            text = "%s, you're not permitted to execute this command." % message.from_info.username
            Messages.palette.custom_answer(message.chat_info.id, text)
    return wrapped

def check_serial_aviability(fn):
    def wrapped(message):
        if config.serial_initialized:
            fn(message)
        else:
            chat_id = message.chat_info.id
            text = "No connection through serial port. =("
            Messages.palette.custom_answer(chat_id, text)
    return wrapped

    
def alarm(text):
    for admin, admin_chat_id in users.get_subscribers().items():
            Messages.palette.custom_answer(admin_chat_id, text)
    