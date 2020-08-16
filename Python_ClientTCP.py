__author__ = 'Gerrit Mulder'
# Name: Gerrit Mulder

import socket

# The Port and IP for the that the client will connect to.
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

# Connects to the server
print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


print ("Connection to Server Established. Please enter the message you would like to send.")
print ("Commands that can be used: \"What is the current date and time?\" and \"exit\"")

# While loop for waiting for the user to enter a command.
while True :
    message = input("Please enter a command: ")
    s.sendall(message.encode()) # Sends the message to the server.

    # Breaks out of the while loop if the user exits.
    if message == "exit" :
        print("client exit")
        break

    # Receives and prints the data from the server.
    data = s.recv(1024)
    print(data.decode())

s.close()
