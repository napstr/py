import os,time,sys
from ipaddress import *
from urllib.request import urlopen
from json import load

#from mylib.Console import *

os.system("")

def loading(i):
    for i in range(0, 101):
        time.sleep(0.05)
        print("\u2592"* int(i/4) + f" Loading {i}% \u2592",end="\r")
        #sys.stdout.flush()
    print()

def titlecolor(col):
    print(f'\x1b[38;2;{col}m title1 \x1b[48;5;235m title2 \x1b[0m')

def title(string):
    string = str(string)
    fcolor = "\u001b[38;2;255;200;0m"
    bcolor = "\u001b[48;5;235m"
    nocolor = "\u001b[0m"
    l="\u2550"
    slen = len(string)
    l= l*(slen +0)
    print(f"{fcolor}{bcolor}\u2554{l}\u2557")   
    print(f"\u2551{bcolor}"+string +f"\u2551{nocolor}")
    print(f"{fcolor}{bcolor}\u255A{l}\u255D{nocolor}") 

def prompt(msg):
    i = input("\u001b[48;5;235m [?] " + msg + ": \u001b[0m ")
    return i

def printx(label,msg):
    print(f" {label} :  \u001b[48;5;235m \u001b[38;2;255;200;0m" + str(msg) + "\u001b[0m")



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
