#!/usr/bin/python

import sys
import socket

UDP_SERVER_HOST = "192.168.xxx.xxx"
UDP_SERVER_PORT = 7090

def print_usage():
  print("This program requires arguments to be passed. Possible arguments are: ")
  print("['i', 'failsafe', 'curr', 'report 1', 'ena 1']")
  print("\nUsage: python " + sys.argv[0] + " i\n")
  exit()

args = len(sys.argv)
if args == 1:
  print_usage()

serverAddressPort = (UDP_SERVER_HOST, UDP_SERVER_PORT)
UDPClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytesSent = UDPClientSock.sendto(str.encode(sys.argv[1]), serverAddressPort)

print ("Successfully sent '{}' ({} bytes) to the server!".format(sys.argv[1], str(bytesSent)))
