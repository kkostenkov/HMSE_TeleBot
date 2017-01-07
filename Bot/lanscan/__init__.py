import config
from lanscan.lanscan import *

class LanScanner():
    known_online_hosts = []
    scan_frequency = 10 # default

    def __init__(self, event_handler):
        
        scan_frequency = config.wifi_scan_frequency
        # Run loop.
        self.lanscan_loop(event_handler)
    
    def get_online_hosts(self):
        ip_range = ["192.168.100." + str(a) for a in range(20)]
        #print (ip_range)
        online_hosts = scan_ip_range(ip_range)
        return online_hosts
        
    def diff(self):
        fresh_online_hosts = self.get_online_hosts()    
        new_hosts = []
        disappeared_hosts = []
        for host in fresh_online_hosts:
            if host in self.known_online_hosts:
                # not new
                continue
            new_hosts.append(host)
        
        for host in self.known_online_hosts:
            if host in fresh_online_hosts:
                # didn't disappear
                continue
            disappeared_hosts.append(host)
        
        i = 0
        new_known_hosts = []
        for host in fresh_online_hosts:
            new_known_hosts.append(fresh_online_hosts[i])
            i += 1
        # Update data.
        self.known_online_hosts = new_known_hosts
        
        #print_diff(new_hosts, disappeared_hosts)
        return {
                "new" : new_hosts,
                "disappeared" : disappeared_hosts,
                }

    def lanscan_loop(self, event_handler):
        # do job
        #print("getting diff")
        diff_info = self.diff()
        #print("got diff.")
        new_users = diff_info.get("new", None)
        if (new_users):
            #print("new:")
            for user in new_users:
                #print(user + " apeared")
                event_handler.call("new_mac_found", [user])
        disappeared_users = diff_info.get("disappeared", None)
        if (disappeared_users):
            #print("old:")
            for user in disappeared_users:
                #print(user + " disappeared")
                event_handler.call("mac_lost", [user])
                continue
        # scedule itself
        t = threading.Timer(self.scan_frequency, self.lanscan_loop, [event_handler])
        t.daemon = True
        t.start()
        
    def print_diff(self, new_hosts, disappeared_hosts):
        if (len(new_hosts) > 0):
            print("________NEW ___________")
            print (new_hosts)
        if (len(disappeared_hosts) > 0):
            print("________ DISAPPEARED ___________")
            print (disappeared_hosts)

def run_lanscan_loop(event_handler):
    LanScanner(event_handler)
    


