#!usr/bin/python3

#
# Class should load events to track from file (xml?, json?)
# Should fire event on it's tracking time
# Should reschedule itself if it is an repeating event.
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
        self.check_events()
        # Schedule itself
        t = threading.Timer(self.loop_frequency, self.schedule_loop)
        #t.daemon = True
        t.start()
        
    def check_events(self):
        now = time.time()
        print(".")
        for event in self.scheduled_events:
            if event.next_fire_time < now:
                self.fire_event(event)
                if event.repeat_interval:
                    print("Requeued")
                    event.next_fire_time += event.repeat_interval
                else:
                    self.remove(event)
                
    def fire_event(self, event):
        print("%s \n Event fired: %s \n %s" % (time.asctime(), event.header, event.message))



if __name__ == "__main__":
    print ("testing Schedule module.")
    import time
    e = EventData("Caption!",
                  "This is first text notification.",
                  time.time() + 2, # Seconds
                  )
    e2 = EventData("Re!",
                  "This is repeating notification.",
                  time.time() + 3, # Seconds
                  repeat_interval=2
                  ) 
    sch = Schedule()
    sch.add(e)
    sch.add(e2)
    
    #for event in sch.scheduled_events:
    #    print(event.header)
    
    sch.schedule_loop()
