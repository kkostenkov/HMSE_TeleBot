from config import admins
import Messages.palette

def notify_admins(fn):
    def wrapped(bot, message):
        sender = message.from_info.username
        action = message.text
        chat_id = message.chat_info.id
        
        for admin in admins:
            print ("Notify %s of \n %s asked for %s" % (admin, sender, action)) # !TODO  messaging notifications
        fn(bot, message)
    return wrapped
    
    
def authentificate(fn):
    def wrapped(bot, message):
        sender = message.from_info.username
        if sender in admins:
            fn(bot, message)
        else:
            text = "%s, you're not permitted to execute this command." % message.from_info.username
            Messages.palette.custom_answer(bot, message.chat_info.id, text)
    return wrapped
    
    
