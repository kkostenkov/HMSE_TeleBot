import os
import subprocess
import threading
from queue import Queue
import config

class BluetoothWorker():
    known_online_hosts = set()
    known_devices = {
        "kirill": "74:23:44:A3:24:4E", 
        "vika": "someaddress",
        }

    def __init__(self, event_handler):        
        self.scan_frequency = config.bt_rollcall_freq
        self.run_main_loop(event_handler)
        
    def run_main_loop(self, event_handler):
        self.do_rollcall()
        self.report(event_handler)
        # scedule itself
        t = threading.Timer(self.scan_frequency, self.run_main_loop, [event_handler])
        t.daemon = True
        t.start()
        
    def do_rollcall(self):
        #print("bt rollcall started")
        for name in self.known_devices:
            mac_id = self.known_devices[name]     
            online = self.check_online(mac_id)
            if online:
                self.known_online_hosts.add(name)
            else:
                self.known_online_hosts.discard(name)
        #print("bt rollcall finished")
        
    def check_online(self, mac_id):
        if os.name == "nt":
            print("bluetooth rollcall not coded for Win yet.")
        else:
            get = subprocess.getoutput("hcitool name " + mac_id)
        if len(get) > 0:
            print("found device" + get)
        return len(get) > 0
        
    def report(self, event_handler):
        event_handler.call("report_bt_rollcall", self.known_online_hosts)
        
def run_worker(event_handler):
    BluetoothWorker(event_handler)
