import socket

HOST = "127.0.0.1"
PORT = 9876


def main():
    # Create a socket that uses ip4 (AF_INET), and TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    while True:
        # Wait for connection, BLOCKING
        client_socket, client_address = server_socket.accept()
        print(f'Client connect from {client_address}')
        # Get data from client, BLOCKING
        message = client_socket.recv(1024)
        message = message.decode('utf-8')
        print("Got message", message)
        return_message = "We got: " + message
        client_socket.send(return_message.encode('utf-8'))


if __name__ == '__main__':
    main()
