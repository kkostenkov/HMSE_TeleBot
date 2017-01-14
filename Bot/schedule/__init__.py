#!usr/bin/python3

#
# Class should load events to track from file (xml?, json?)
# Should fire event on it's tracking time
# Should reschedule itself if it is an repeating event.
#

import threading, time
from schedule.event_data import EventData


class Schedule():
    scheduled_events = []
    loop_frequency = 1 # Check every second
    
    def __init__(self):
        pass
        
    def add(self, event):
        self.scheduled_events.append(event)
        
    def remove(self, event):
        self.scheduled_events.remove(event)
        
    def schedule_loop(self):
        self.check_events()
        t = threading.Timer(self.loop_frequency, self.schedule_loop)
        #t.daemon = True
        t.start()
        
    def check_events(self):
        now = time.time()
        print(".")
        for event in self.scheduled_events:
            if event.next_fire_time < now:
                if event.action:
                    event.action()
                if event.repeat_interval:
                    print("Requeued")
                    event.next_fire_time += event.repeat_interval
                else:
                    self.remove(event)


if __name__ == "__main__":
    print ("testing Schedule module.")
    import time
    e = EventData("Caption!",
                  "This is first text notification.",
                  time.time() + 50, # Seconds
                  )
    e2 = EventData("Re!",
                  "This is repeating notification.",
                  time.time() + 50,
                  repeat_interval=10
                  )
                  
    def sample_test_callback(): print("ACTIOOOON!")
    
    e3 = EventData("Action!",
                  "Let's call some func.",
                  time.time() + 20,
                  #repeat_interval=10,
                  callback = sample_test_callback
                  )
    e4 = EventData("lambda action!",
                  "Let's call some stored lambda.", 
                  time.time() + 30, 
                  #repeat_interval=2, 
                  callback = lambda:  print("lambda called") 
                  )
    someData = EventData("data STAYS the same", "data text to lambda", time.time() + 1)
    e5 = EventData("lambda action with args!",
                  "Let's call some stored lambda with args.", 
                  time.time() + 1, 
                  repeat_interval=2, 
                  callback = lambda :  print(someData.header)
                  )
    someData = EventData("it does not", "data text to lambda", time.time() + 1)

    some_lambda_var = 10
    sch = Schedule() 
    sch.add(e) 
    sch.add(e2) 
    sch.add(e3) 
    sch.add(e4)
    sch.add(e5)

    #for event in sch.scheduled_events:
    #    print(event.header)
    
    sch.schedule_loop()
