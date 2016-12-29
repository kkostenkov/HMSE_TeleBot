
notification_subscribers = {}

def add_subscriber(name, chat_id):
    notification_subscribers[name] = chat_id
    
def get_subscribers():
    return notification_subscribers