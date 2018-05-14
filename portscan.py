#!/usr/bin/python
from socket import *
import sys
import time

#default socket connection time out
DefaultTimeOut = 0.30

#portScan function takes the hostname/port address, a start port and an end port for the scan 
def portScan(hostname, startPort, endPort):
	try:
		targetServer = hostname
		targetIP = gethostbyname(targetServer)
		print "\nScanning ports on " + hostname
		print "IP of the host is " + targetIP +"\n"
		print "Please wait! Generating scan report for " + hostname + "\n"
		
		#Scan ports in the given range
		for i in range(startPort, endPort+1 ):
			s = socket(AF_INET, SOCK_STREAM)
			s.settimeout(DefaultTimeOut)
			result = s.connect_ex((targetIP, i))
			if(result == 0):
				print "[+] Port %d is open" % (i,)
			s.close()
		return True
	except Exception, e:
		return False

#take user inputs from the terminal
hostname = sys.argv[1]
startPort = int(sys.argv[2])
endPort = int(sys.argv[3])

#invoke portScan function 
portScan(hostname, startPort, endPort)
print "\nEnd of Scan........."

