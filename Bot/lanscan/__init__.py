from lanscan import *

known_online_hosts = [[],]

def get_online_hosts():
    ip_range = ["192.168.100." + str(a) for a in range(20)]
    #print (ip_range)
    online_hosts = scan_ip_range(ip_range)
    return online_hosts
    

def diff():
    fresh_online_hosts = get_online_hosts()    
    new_hosts = []
    disappeared_hosts = []
    for host in fresh_online_hosts:
        if host in known_online_hosts[0]:
            # not new
            continue
        new_hosts.append(host)
    
    for host in known_online_hosts[0]:
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
    known_online_hosts[0] = new_known_hosts
    
    #if (len(new_hosts) > 0):
    #    print("________NEW ___________")
    #    print (new_hosts)
    #if (len(disappeared_hosts) > 0):
    #    print("________ DISAPPEARED ___________")
    #    print (disappeared_hosts)
    return {
            "new" : new_hosts,
            "disappeared" : disappeared_hosts,
            }

scan_frequency = 10 # once every %scan_frequency% seconds 
def lanscan_loop():
    # do job
    print("getting diff")
    diff_info = diff()
    print("got diff.")
    new_users = diff_info.get("new", None)
    if (new_users):
        print("new:")
        for user in new_users:
            print(user + " apeared")
    disappeared_users = diff_info.get("disappeared", None)
    if (disappeared_users):
        print("old:")
        for user in disappeared:
            print(user + " disappeared")
    # scedule itself
    t = threading.Timer(scan_frequency, lanscan_loop)
    t.daemon = True
    t.start()

def run_lanscan_loop():
    lanscan_loop()


if __name__ == "__main__":
    run_lanscan_loop()
    import time
    while(True):
        time.sleep(10)
