__author__ = 'Gerrit Mulder'
# Name: Gerrit Mulder

import socket
from datetime import datetime

# The Port, IP, and Buffer for the server.
UDP_IP = '127.0.0.1'
UDP_PORT = 5005
UDP_Buffer = 1024

# Creates the socket and binds it to the address and IP
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

# Loops and waits for messages from clients.
while (True) :

    # Receives data from the client.
    bytes_address = s.recvfrom(UDP_Buffer)
    data = bytes_address[0]
    address = bytes_address[1]

    temp = data.decode() # Decodes the data so we can look at it.

    if temp == "What is the current date and time?" : # if the client asks for the current dat & time then send it to them.
        date_time = datetime.today().strftime('%m/%d/%Y %H:%M:%S')
        message = "Current Date and Time – " + date_time
        temp2 = message.encode() # Encode the data so we can send it.
        s.sendto(temp2, address)
    else : # The message from the client is unknown so return an invalid request message.
        message = "Error invalid request. Please enter a valid request. Valid requests are \"What is the current date and time?\""
        temp2 = message.encode()
        s.sendto(temp2, address)