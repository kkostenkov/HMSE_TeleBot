import config
from data import users
import Messages.palette

def notify_admins(fn):
    def wrapped(bot, message):
        sender = message.from_info.username
        action = message.text
        text = "%s asked for %s" % (sender, action)
        for admin, admin_chat_id in users.get_subscribers().items():
            Messages.palette.custom_answer(bot, admin_chat_id, text)
        fn(bot, message)
    return wrapped
    
    
def authentificate(fn):
    def wrapped(bot, message):
        sender = message.from_info.username
        if sender in config.admins:
            fn(bot, message)
        else:
            text = "%s, you're not permitted to execute this command." % message.from_info.username
            Messages.palette.custom_answer(bot, message.chat_info.id, text)
    return wrapped

def check_serial_aviability(fn):
    def wrapped(bot, message):
        if config.serial_initialized:
            fn(bot, message)
        else:
            chat_id = message.chat_info.id
            text = "No connection through serial port. =("
            Messages.palette.custom_answer(bot, chat_id, text)
    return wrapped
