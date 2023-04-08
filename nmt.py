import os
import time

def ping_hosts(hostnames):
    for host in hostnames:
        response = os.system("ping -c 1 " + host)
        
        if response == 0:
            print(f"{host} is up!")
        else:
            print(f"{host} is down!")

def monitor_network(hostnames, interval):
    while True:
        ping_hosts(hostnames)
        time.sleep(interval)

if __name__ == "__main__":
    hostnames = ['google.com', 'yahoo.com', 'bing.com']
    interval = 60 # seconds
    
    monitor_network(hostnames, interval)
