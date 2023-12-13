import socket
import threading


def handle_client(client_socket):
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    # Echo the received data back to the client
    client_socket.send(data.encode('utf-8'))

    # Close the client socket
    client_socket.close()


def start_echo_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('127.0.0.1', 8888))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on port 8888...")

    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_echo_server()
