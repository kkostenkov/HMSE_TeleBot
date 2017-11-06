from Messages.administration import alarm
from speech import speech
import time

class HomeEventHandler:
    events = {}
    
    def __init__(self):
        self.register_event("new_mac_found", new_mac_found)
        self.register_event("mac_lost", mac_lost)
        self.register_event("report_bt_rollcall", process_bt_rollcall)
        self.register_event("report_serial_status", process_serial_status)
    
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
              ("38", "a4", "ed", "05", "bd", "02") : "kirill",
              ("f8", "27", "93", "30", "5a", "ca") : "vika",
              }
last_online = {
               "kirill" : 0,
               "vika" : 0,
               }
max_offline_time = 60 * 60 * 5  # seconds              

def new_mac_found(args):
    mac = tuple(args[0])
    username = known_macs.get(mac, None)    
    if (not username):
        #print("Unknown mac appeared")
        return
    update_last_online_time(username)


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
    
def process_bt_rollcall(bt_users_at_place):
    for username in bt_users_at_place:
        update_last_online_time(username)

def update_last_online_time(username):
    was_last_online = last_online[username]
    now = time.time()
    if (was_last_online != 0 and was_last_online < now - max_offline_time ):
        # user was offline for too long. Worth notifying.
        
        gmtime = time.gmtime(was_last_online)
        human_readable_time = time.asctime(gmtime)
        text = "%s found online. Last online time: %s" % (username, human_readable_time)
        # Message
        alarm(text)
        # Text
        print (text)
        # Voice
        speech.ding()
        speech.greet_with_daypart()
        speech.say(username)
    last_online[username] = now
    

last_statuses = {"doorClosed": 1, "temp": "Not meashured"}    
 
def process_serial_status(status):
    new_door_closed_status = status.get("doorClosed")
    if (new_door_closed_status == None): 
        print("Door info not in status")
        return
    if not new_door_closed_status and last_statuses["doorClosed"]:
        text = "Door opened"
        print(text)
        alarm(text)
    last_statuses["doorClosed"] = new_door_closed_status
