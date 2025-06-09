# use the following modules for developing your code 
#  wherever you see "#...", it means you may need to provide some codes

import socket
import threading
import queue


#...


# complete the receive_messages function
def receive_messages(client_socket):
    while True:
        try:
            # complete receiving the message from the server
            #...
            pass
        except: 
            #...
            print("Connection closed or error receiving message.")
            break

# complete the client_program function
def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9000))
    #...
   

    while True:
        #...

        print("\nOptions:")
        print("1. List: View all connected users.")
        print("2. Send: Send a message to a user.")
        print("3. Exit: Exit the program.")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            #...
            pass
            
        elif choice == "2":
            #...
            pass
        
        elif choice == "3":
            #...
            pass
         
        else:
            #...
            pass


if __name__ == "__main__":
    client_program()
