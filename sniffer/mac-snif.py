'''
Created on 6 Jun 2021

@author: adam
'''

#!/usr/bin/python3

import socket
from struct import *

#eth_addr() takes as arg, each byte of type char from the received packet[0]
#format string % is place holder .2x attaches two hexadecimal numbers

#the ord() function takes the binary numbers and converts them to a ASCII
#ord() FUNCTION NOT NEED IN PYHTON3 due to socket.recvfrom returns string pair (bytes, address)
#python2 socket.recvfrom returns pair (string, address) and therefor ord function would be needed

#char characters which are placed in the string %.2x 
#the string is stored in variable mac_address and retured from function
#to be printed out below on lines 89 and 90 
def eth_addr(mac_char):
    mac_address = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x:" % ((mac_char[0]), 
                                                      (mac_char[1]), 
                                                      (mac_char[2]), 
                                                      (mac_char[3]),
                                                      (mac_char[4]), 
                                                      (mac_char[5]),)
    return mac_address

#ntohs() function of socket module converts mac_char 16 bit integer
#from network format to host format. 
#parameter 0x0003 in hexadecimal for the number 3 and we are using 
#GGP protocol. you can also do the same using getprotoent("GGP")
#socket.ntohs(0x0003)

try:                                                     
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
    print("[!!] Error on creating socket object")
    exit(0)

#The recvfrom() method Python's socket class, reads a number of bytes sent from a socket.

#The return value is a pair (string, address) where string is a string representing
#the data (remember data is in bytes!) received and address is the address of the socket sending the data.

#s.recvfrom() parameter 65535 is port number.
#This will first recive packet from port 1 then 2 and so on ...
#untill it reaches port 65535 as is inside the while Ture loop.

while True:
    #setting the packet to recive the first part of the tuple
    #a string in bytes format. The second part, packet[1]
    #would be the address as stated on lines 45 and 46
    packet = s.recvfrom(65535)
    
    packet = packet[0]
    
    #selecting first 14 bytes from first packets[0]
    #the first 14 bytes holds the ether info 
    eth_lenght = 14
    eth_header = packet[:eth_lenght] 
    
    #unpack from struct takes binary data from C structs and corectly formats it 
    
    #First parameter ! is the format type (network=big-endian) of data
    #there are other formats that can be use !, @, =, <, and >
    
    #6 is the number of bytes from the eth_header
    #s identifies these 6 bytes as a char[] (string). the first 6 bytes are the 
    #destination mac address. 
    
    #We then do the same to get the next 6 bytes
    #which is the source mac address.
    
    #Finally we have the H parameter which is the ether protocol. The type is an
    #unsigned short. (an unsigned short is 2 bytes) 
    #this all together makes 14 bytes
    eth = unpack('!6s6sH', eth_header)
    
    #Saving the 3rd eliment from eth object above. eth[2] which is H. This is 
    #the ether protocol which is a number representing tcp, udp, http ect ...
    #agine we use socket.ntohs to convert to host format 
    #(ntohs Convert 16-bit positive integers from network to host byte order)
    eth_protocol = socket.ntohs(eth[2])
    
    #Now we must print out the formatted data to show dst MAC, src MAC, and 
    #eth_protocol. For dst and src MAC we will need a function eth_addr to
    #print out the binary data in a string format. But as for eth_protocol we 
    #can just cast to a string str(eth_protocol) as we have already separated 
    #this binary data and stored it in the vriable eth_protocol on line 82
    print('[+] Destination MAC:' + eth_addr(packet[0:6]) + '[+] Source MAC:' +
          eth_addr(packet[6:12]) + '[+] Protocol: ' + str(eth_protocol))   
    
    
    
    
