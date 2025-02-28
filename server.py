import socket

# Define server settings
HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 12345      # Port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Bind to the specified IP and port
server_socket.listen(1)  # Listen for incoming connections

print(f"Server is listening on {HOST}:{PORT}...")

# Accept connection from client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Chat loop
while True:
    data = client_socket.recv(1024).decode()  # Receive message
    if not data or data.lower() == "exit":
        print("Client has left the chat.")
        break
    print(f"Client: {data}")

    message = input("You: ")  # Get server response
    client_socket.send(message.encode())  # Send message

# Close sockets
client_socket.close()
server_socket.close()
