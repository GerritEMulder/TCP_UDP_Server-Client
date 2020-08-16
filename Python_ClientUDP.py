__author__ = 'Gerrit Mulder'
# Name: Gerrit Mulder

import socket

# The Port and IP for the that the client will connect to.
UDP_IP = '127.0.0.1'
UDP_PORT = 5005
UDP_Buffer = 1024

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # Creates the socket.

print ("Please enter the message you would like to send.")
print ("Command that can be used: \"What is the current date and time?\"")

# While loop for waiting for the user to enter a command.
while True :
    message = input("Please enter a command: ")
    bytemessage = message.encode() # Encode the data so we can send it.
    s.sendto(bytemessage, (UDP_IP, UDP_PORT)) # Sends the data to the UDP server.

    # Receives the message from the server and then prints that message to the screen.
    message_server = s.recvfrom(UDP_Buffer)
    converted_message = message_server[0].decode()
    print(converted_message)