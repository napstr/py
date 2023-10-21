import socket

# TCP Client -Example

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data.encode("utf-8"))

# receive some data
response = client.recv(4096).decode("utf-8")

# show
print(response)
