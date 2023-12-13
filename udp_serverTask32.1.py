#  UDP Server:

import socket

server_address = ('localhost', 5555)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind(server_address)

print(f"UDP server is listening on {server_address}")

while True:
    # Wait for incoming messages
    data, client_address = server_socket.recvfrom(1024)

    print(f"Received message from {client_address}: {data.decode('utf-8')}")

    # Optionally, send a response back to the client
    response = "Message received!"
    server_socket.sendto(response.encode('utf-8'), client_address)
