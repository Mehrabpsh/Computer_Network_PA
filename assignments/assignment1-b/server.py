# use the following modules for developing your code.
#  wherever you see "#...", it means you may need to provide some codes
import socket
import threading

#...

# complete handle_client
def handle_client(client_socket, client_address):

    username = client_socket.recv(1024).decode('utf-8')
    print(f"{username} connected from {client_address}")

    #...

    while True:
        try:
            
            message = client_socket.recv(1024).decode('utf-8')

            # complete handling "list" command here
            if message.lower() == "list":
                # You need to implement the logic to send a list of users
                #...
                pass

            # complete handling "send" command here
            elif message.lower().startswith("send"):
                # You need to implement logic to send message to recipient
                #...
                pass

            # complete handling "exit" command here
            elif message.lower() == "exit":
                # You need to implement the disconnection logic
                #...
                pass

            else:
                # Handle invalid command
                #...
                pass

        except:
            # Handle connection errors and cleanup
            #...
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9000))
    server.listen(5)
    print("Server started on port 9000...") 

    # complete here: accept incoming connections & ...
    while True:
        client_socket, client_address = server.accept()
        #...
        pass

if __name__ == "__main__":
    start_server()
