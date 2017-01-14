#!usr/bin/python3

#
# Class should load events to track from file (xml?, json?)
# Should fire event on it's tracking time
# Should reschedule itself if it is an repeating event.
# 
#

import threading
from event_data import EventData


class Schedule():
    scheduled_events = []
    loop_frequency = 1 # Check every second
    
    def __init__(self):
        pass
        
    def add(self, event):
        self.scheduled_events.append(event)
        
    def remove(self, event):
        self.scheduled_events.remove(event)

    def load_event_from_dict(self):
        pass
        
    def schedule_loop(self):
        # Check for events to fire
        self.fire_events()
        # Schedule itself
        t = threading.Timer(self.loop_frequency, self.schedule_loop)
        #t.daemon = True
        t.start()
        
    def fire_events(self):
        now = time.time()
        print(now)
        for event in self.scheduled_events:
            if event.next_fire_time < now:
                print("Event fired: %s \n %s" % (event.header, event.message))


if __name__ == "__main__":
    print ("testing Schedule module.")
    import time
    e = EventData("Caption!",
                  "This is first text notification.",
                  time.time() + 5, # Seconds
                  repeating=False)
    print(e.message)              
    sch = Schedule()
    sch.add(e)
    
    for event in sch.scheduled_events:
        print(event.header)
    
    sch.schedule_loop()
