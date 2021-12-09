import socket

HOST = '127.0.0.1'
PORT = 9876


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    while True:
        # Get user message - BLOCKING
        message = input("Enter something> ")
        # Send the message
        client_socket.send(message.encode('utf-8'))
        # Receive message from server - BLOCKING
        message = client_socket.recv(1024)
        message = message.decode('utf-8')
        print(message)


if __name__ == '__main__':
    main()
