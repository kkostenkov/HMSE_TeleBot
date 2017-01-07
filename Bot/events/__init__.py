from Messages.administration import alarm
from speech import speech
import time

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
last_online = {
               "Keeps" : 0,
               "Victory" : 0,
               }
max_offline_time = 60 * 120  # seconds              

def new_mac_found(args):
    mac = tuple(args[0])
    username = known_macs.get(mac, None)    
    if (not username):
        #print("Unknown mac appeared")
        return
    was_last_online = last_online[username]
    now = time.time()
    if (was_last_online != 0 and was_last_online < now - max_offline_time ):
        # user was offline for too long. Worth notifying.
        human_readable_time = time.asctime(time.gmtime(was_last_online))
        text = "%s found online. Last online time: %s" % (username, human_readable_time)
        speech.ding()
        print (text)
        alarm(text)
    last_online[username] = now

def mac_lost(args):
    mac = tuple(args[0])
    username = known_macs.get(mac, None)    
    if (not username):
        #print("Unknown mac lost")
        return
    text = username + " lost connection"
    #speech.ding()
    print (text)
    #alarm(text)
