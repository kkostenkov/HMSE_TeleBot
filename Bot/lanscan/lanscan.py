import os
import subprocess
#import config

def ip_is_online(ip):
    try:
        if os.name == "nt":
            get = subprocess.getoutput("ping " + ip + " -n 1 -w 100")
        else:
            get = subprocess.getoutput("ping " + ip + " -c 1")
    except OSError:
        print("Cannot execute ping, propably you dont have enough permissions to create process")
        sys.exit(1)
    Lines = get.split("\n")
    for line in Lines:
        # find line where is timing given
        if os.name == "nt":
            if line.find("TTL") > -1:
                return True
        else: 
            if line.find("icmp_") > -1:
                Exp = line.split('=')
                # if response is valid
                if len(Exp) == 4:
                    #self.Status = Exp[3].replace(' ms', '')
                    return True
        
    #print("%s, down" % ip)    
    return False  
    
def scan_ip_range(ip_range):
    alive_hosts = []
    online_macs = []
    for IPAdress in ip_range:
        # !TODO Validate ip
        if ip_is_online(IPAdress): # !TODO multithread
            #print("%s is alive" % IPAdress)
            alive_hosts.append(IPAdress)
            mac = get_mac(IPAdress)
            if (mac):
                #print(mac)
                online_macs.append(mac)
    return online_macs

def get_mac(ip):
    import os,re
    get = subprocess.getoutput("arp -a " + ip)    
    X = '([a-fA-F0-9]{2}[:|\-]?){6}' 
    a = re.compile(X).search(get)
    if a:
        return (get[a.start(): a.end()])
              
if __name__ == "__main__":
    ip_range = ["192.168.100." + str(a) for a in range(15)]
    #print (ip_range)
    online_hosts = scan_ip_range(ip_range)
        
    