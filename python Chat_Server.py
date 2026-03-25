import socket
import threading

# Function to receive messages from client
def receive_messages(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print("\nClient:", message)
            else:
                break
        except:
            break

# Function to send messages to client
def send_messages(conn):
    while True:
        message = input()
        conn.send(message.encode())

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind (use your IP if using different devices)
server.bind(("0.0.0.0", 5000))

server.listen(1)
print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

# Run send & receive simultaneously
threading.Thread(target=receive_messages, args=(conn,)).start()
threading.Thread(target=send_messages, args=(conn,)).start()