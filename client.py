import socket

# Define server settings
SERVER_IP = "127.0.0.1"  # Change this to the actual server's IP if running on different machines
PORT = 12345             # Port number

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_IP, PORT))
print("Connected to the server. Type 'exit' to leave the chat.")

# Chat loop
while True:
    message = input("You: ")  # Get user message
    client_socket.send(message.encode())  # Send message to server

    if message.lower() == "exit":
        break

    data = client_socket.recv(1024).decode()  # Receive response from server
    print(f"Server: {data}")

# Close socket
client_socket.close()
