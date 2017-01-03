from lanscan import *

known_online_hosts = []

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
        if host in known_online_hosts:
            # not new
            continue
        new_hosts.append(host)
    
    for host in known_online_hosts:
        if host in fresh_online_hosts:
            # didn't disappear
            continue
        disappeared_hosts.append(host)
    
    known_online_hosts.clear()
    i = 0
    for host in fresh_online_hosts:
        known_online_hosts.append(fresh_online_hosts[i])
        i += 1
    
    print("________NEW ___________")
    print (new_hosts)
    print("________ DISAPPEARED ___________")
    print (disappeared_hosts)
    return {
            "new" : new_hosts,
            "disappeared" : disappeared_hosts,
            }
        


if __name__ == "__main__":
    import time
    while True:
        diff()
        time.sleep(10)