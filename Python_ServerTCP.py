__author__ = 'Gerrit Mulder'
# Name: Gerrit Mulder

import socket
from datetime import datetime

# The Port and IP for the server.
TCP_IP = '127.0.0.1'
TCP_PORT = 5005

# While loop for waiting for new client connections.
while True :
    
    # Creates the socket and binds it to the address and IP.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1) # Waits for a connection.

    conn, addr = s.accept()

    print('Server Address:', TCP_IP)
    print('Client Address:', addr)
    print("Connection to Client Established, Waiting to Receive Message...")
    s.listen(1)

    # Loops while the client is connected.
    while (True) :

        # Try to receive data from the client.
        try:
            data = conn.recv(1024)
            temp = data.decode() # Decodes the data so we can look at it.

            # If the client asks for the current date and time then send them that information.
            if temp == "What is the current date and time?" :
                date_time = datetime.today().strftime('%m/%d/%Y %H:%M:%S')
                message = "Current Date and Time – " + date_time
                conn.sendall(message.encode())
            elif temp == "exit" : # The client is disconnecting so break out of the loop and wait until a new client connects.
                break
            else : # The message from the client is unknown so return an invalid request message.
                message = "Error invalid request. Please enter a valid request. Valid requests are \"What is the current date and time?\" and \"exit\""
                conn.sendall(message.encode())
            s.listen(1)

        # If the socket disconnects or has some error with it, break out of the loop and go back to waiting for a new connection. 
        except socket.error:
            break

