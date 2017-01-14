#
# Contans all data for any event to schedule.
#

import time

class EventData:
    header = ""
    message = ""
    
    repeating = False
    next_fire_time = None
    

    def __init__(self, header, message, next_fire_time, 
                 repeat_interval=None, action=None):
        self.header = header
        self.message = message
        self.next_fire_time = next_fire_time
        
        self.repeat_interval = repeat_interval # seconds
        self.action = action

