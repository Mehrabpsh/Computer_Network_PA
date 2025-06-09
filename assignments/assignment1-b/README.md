# Assignment 2: Socket Programming - Multi-Client Chatroom

## Objective
In this assignment, you will build a **multi-client chatroom** using **Socket Programming**. You will implement two programs: a **server** and a **client**. The server listens for connections, while clients interact with it by sending messages and querying connected users.

## Scaffolding
The provided files are **scaffolded** with placeholders. Wherever you see `#...`, you need to complete the logic. This will guide you through building the necessary functionality for both the server and client.

## Requirements

### **Server**:
- Listen on **port 9000**.
- Store each client’s **username**, **IP address**, and **port number**.
- Handle the following commands from clients:
  - **List**: Return a list of all connected users.
  - **Send**: Forward a message to the specified recipient.
  - **Exit**: Disconnect the client and remove it from the list.

### **Client**:
- Prompt the user for a **username** and establish a connection to the server.
- Provide a menu with the following options:
  1. **List**: Display all connected users.
  2. **Send**: Send a message to another user.
  3. **Exit**: Exit the chat program.
- Continuously listen for incoming messages from other users.

### **Additional Notes**:
- The **server** must handle multiple clients at once using **threads**.
- The **client** program should be able to handle sending and receiving messages simultaneously using **threading** and a **message queue**.

## Testing
1. SSH into your virtual machine using the command `vagrant ssh` (as prepared in the previous assignment).
2. Run one instance of the **server** program.
3. Launch **5 clients** with different usernames to test communication:
   - Check the **List** command to see all connected users.
   - Send and receive messages between clients.
   - Test proper handling of the **Exit** command.

## Submission
Submit your completed **client.py** and **server.py** programs to: [Programming Assignment 2](https://elearn.ut.ac.ir). Ensure your code is well-commented, especially where you complete the scaffolding sections.
