import os,time,sys
from ipaddress import *
from urllib.request import urlopen
from json import load

#from mylib.Console import *

os.system("")

def loading(i):
    for i in range(0, 101):
        time.sleep(0.05)
        print("-"* int(i/4) + f" Loading {i}% \u2592",end="\r")
        #sys.stdout.flush()
    print()



def title(string):
    string = str(string)
    fcolor = ""
    bcolor = ""
    nocolor = ""
    l=""
    slen = len(string)
    l= l*(slen +0)
    print(f"{fcolor}{bcolor}4{l}")   
    print(f"{bcolor}"+string +f"{nocolor}")
    print(f"{fcolor}{bcolor}{l}{nocolor}") 

def prompt(msg):
    i = input(" [?] " + msg + ": ")
    return i

def printx(label,msg):
    print(f" {label} : " + str(msg) + " ")



title("      ~: IP INFORMATION :~      ")

ip_ = "192.168.1.1"

def ipInfo(addr = ''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = (f"https://ipinfo.io/{addr}/json")

    
    res = urlopen(url)
    data = load(res)

    for attr in data.keys():
        #will print the data line by line
        printx(" "+ attr,data[attr])

    # will load JSON response
    ip4 = IPv4Address('192.168.1.1')
    printx(" Version",str(ip4.version))
    printx(" DNS PTR",ip4.reverse_pointer)
    printx(" Is Multicast",ip4.is_multicast)
    printx(" Is Private",ip4.is_private)
    printx(" Is Global",ip4.is_global)
    printx(" Is Unspecified",ip4.is_unspecified)
    printx(" Is Lookback",ip4.is_loopback)
    printx(" Is Reserved",ip4.is_reserved)
    printx(" Is Linked Local",ip4.is_link_local)


p1 = prompt("please enter ip address")
ipInfo(p1)
