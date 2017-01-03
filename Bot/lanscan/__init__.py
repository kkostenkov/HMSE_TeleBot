from lanscan import *

def get_online_hosts():
    ip_range = ["192.168.100." + str(a) for a in range(20)]
    #print (ip_range)
    online_hosts = scan_ip_range(ip_range)
    return online_hosts
    
    
a = get_online_hosts()
print (a)