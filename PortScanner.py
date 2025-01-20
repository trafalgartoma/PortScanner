import sys
import socket
from datetime import datetime

#Ask for input IPv4 Address
target = input("Enter the IP address to scan: ")

#Banner
print("-" * 50)
print("Scanning target "+target)
print("Scanning started at "+str(datetime.now()))
print("-" * 50)

#Scanning ports between 1 to 65535 (this is the cap for ports)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET are IPv4 and SOCK_STREAM is the port number
        socket.setdefaulttimeout(1) 

        #return an error indicator
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:   
    print("Couldn't connect to server.")
    sys.exit()
      