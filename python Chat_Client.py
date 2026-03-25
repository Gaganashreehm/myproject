import socket
import threading

# Function to receive messages from server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print("\nServer:", message)
            else:
                break
        except:
            break

# Function to send messages to server
def send_messages(client):
    while True:
        message = input()
        client.send(message.encode())

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Change IP if connecting to another computer
client.connect(("127.0.0.1", 5000))

print("Connected to server")

# Run both send & receive
threading.Thread(target=receive_messages, args=(client,)).start()
threading.Thread(target=send_messages, args=(client,)).start()