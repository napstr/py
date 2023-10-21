import socket

# Get public IP address using Google
def host_IP():
	try:
		#h_name = socket.gethostname()
		#hip = socket.gethostbyname(hname)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		public_ip = s.getsockname()[0]
		#print("Hostname: {} ".format(h_name))
		#print("IP Address: ",hip)
		print("Public IP Address:",public_ip)
	except:
		print("Unable to get Hostname and IP")

# Driver code
host_IP() #Function call
