import socket


def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def handle_client(client_socket):
    key = int(client_socket.recv(1024).decode())
    print(f"Received key: {key}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        encrypted_data = caesar_cipher(data, key)
        client_socket.send(encrypted_data.encode())

    client_socket.close()


def main():
    server_host = '127.0.0.1'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Accepted connection from {client_addr}")
        handle_client(client_socket)


if __name__ == "__main__":
    main()
