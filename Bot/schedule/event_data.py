#
# Contans all data for any event to schedule.
#

class EventData:
    header = ""
    message = ""
    next_fire_time = None
    
    repeat_interval = None
    callback = None

    def __init__(self, header, message, next_fire_time, 
                 repeat_interval=None, callback=None):
        self.header = header
        self.message = message
        self.next_fire_time = next_fire_time
        
        self.repeat_interval = repeat_interval # seconds
        self.action = callback
