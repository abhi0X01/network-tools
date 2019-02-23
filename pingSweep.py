#! /usr/bin/python2.7
# This script checks the status of hosts in a given subnet 

import subprocess

subnet = raw_input("Enter the subnet you want to sweep: ")
print("Ping sweeping the subnet "+ subnet)
for i in range(1, 254):
	IP = subnet +"."+ str(i)
	result= subprocess.call(['fping' ,'-a', '-q', '-s' , IP]) #show targets that are alive
