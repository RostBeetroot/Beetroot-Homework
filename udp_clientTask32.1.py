# UDP Client:

import socket

server_address = ('localhost', 5555)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter message to send (type 'exit' to quit): ")
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Check if the user wants to exit
    if message.lower() == 'exit':
        break

    # Receive and print the server's response
    response, _ = client_socket.recvfrom(1024)
    print(f"Server response: {response.decode('utf-8')}")

client_socket.close()
