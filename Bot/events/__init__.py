from enum import Enum
from Messages.administration import alarm
from speech import speech

class EventType(Enum):
    nothing = 0
    new_mac = 1

class HomeEventHandler:
    events = {}
    
    def __init__(self):
        self.register_event("new_mac_found", new_mac_found)
        self.register_event("mac_lost", mac_lost)
    
    def register_event(self, name, action):
        #events.add(name, action)
        self.events[name] = action
    
    def call(self, event_name, args):
        action = self.events.get(event_name, None)
        if (not action):
            print("No action found for event %s." % event_name)
            return
        action(args)


known_macs = { 
              ("38", "a4", "ed", "05", "bd", "02") : "Keeps",
              ("f8", "27", "93", "30", "5a", "ca") : "Victory",
              }

def new_mac_found(args):
    mac = tuple(args[0])
    user = known_macs.get(mac, None)    
    if (not user):
        #print("Unknown new mac")
        return
    text = user + " found online"
    speech.ding()
    print (text)
    alarm(text)
    
def mac_lost(args):
    mac = tuple(args[0])
    user = known_macs.get(mac, None)    
    if (not user):
        #print("Unknown new mac")
        return
    text = user + " lost connection"
    speech.ding()
    print (text)
    alarm(text)