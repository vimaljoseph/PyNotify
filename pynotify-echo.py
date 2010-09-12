#!/usr/bin/python
# Client program

from socket import *
import sys
# Set the socket parameters

#host = sys.argv[1]
#print host
host = "192.168.1.255"
port = 8250
buf = 1024
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind((host,0))
UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
def_msg = "===Enter message to send to server===\nBlank line to quit";
print "\n",def_msg

# Send messages
while (1):
	data = raw_input('>> ')
	if not data:
		break
	else:
		if(UDPSock.sendto(data,addr)):
			print "Sending message '",data,"'....."

# Close socket
UDPSock.close()
