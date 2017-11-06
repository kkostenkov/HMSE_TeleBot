from Messages.administration import alarm
from speech import speech
import time

class HomeEventHandler:
    events = {}
    
    def __init__(self):
        self.register_event("new_mac_found", self.new_mac_found)
        self.register_event("mac_lost", self.mac_lost)
        self.register_event("report_bt_rollcall", self.process_bt_rollcall)
        self.register_event("report_serial_status", self.process_serial_status)
    
    def register_event(self, name, action):
        self.events[name] = action
    
    def call(self, event_name, args):
        action = self.events.get(event_name, None)
        if (not action):
            print("No action found for event %s." % event_name)
            return
        action(args)
        
    def set_bt_worker(self, bt_worker):
        self.bt = bt_worker


    known_macs = { 
                  ("38", "a4", "ed", "05", "bd", "02") : "kirill",
                  ("f8", "27", "93", "30", "5a", "ca") : "vika",
                  }
    last_online = {
                   "kirill" : 0,
                   "vika" : 0,
                   }
    max_offline_time = 60 * 60 * 5  # seconds              

    def new_mac_found(self, args):
        mac = tuple(args[0])
        username = self.known_macs.get(mac, None)    
        if (not username):
            #print("Unknown mac appeared")
            return
        self.update_last_online_time(username)


    def mac_lost(self, args):
        mac = tuple(args[0])
        username = self.known_macs.get(mac, None)    
        if (not username):
            #print("Unknown mac lost")
            return
        text = username + " lost connection"
        #speech.ding()
        print (text)
        #alarm(text)
        
    def process_bt_rollcall(self, bt_users_at_place):
        for username in bt_users_at_place:
            self.update_last_online_time(username)

    def update_last_online_time(self, username):
        was_last_online = self.last_online[username]
        now = time.time()
        if (was_last_online != 0 and was_last_online < now - self.max_offline_time ):
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
        self.last_online[username] = now
        

    last_statuses = {"doorClosed": 1, "temp": "Not meashured"}    
     
    def process_serial_status(self, status):
        new_door_closed_status = status.get("doorClosed")
        if (new_door_closed_status == None): 
            print("Door info not in status")
            return
        if not new_door_closed_status and self.last_statuses["doorClosed"]:
            text = "Door opened"
            print(text)
            alarm(text)
            self.check_who_is_home()
        self.last_statuses["doorClosed"] = new_door_closed_status
        
    def check_who_is_home(self):
        if self.bt is None:
            return
        self.bt.rollcall_and_report(self)
