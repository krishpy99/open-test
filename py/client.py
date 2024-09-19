import socket
import select
import sys

client_socket = socket.socket()

if len(sys.argv) != 3:
    print("Need script, IP and port")
    exit()

IP = str(sys.argv[1])
Port = int(sys.argv[2])

client_socket.connect((IP, Port))

while True:

    sockets_list = [sys.stdin, client_socket]

    read_sockets, write_socket, err = select.select(sockets_list, [], [])

    for _socket in read_sockets:
        if _socket == client_socket:
            message = _socket.recv(2048)
            print(message)
        else:
            message = sys.stdin.readlin()
            client_socket.send(message)
            sys.stdout.write("<You>: ")
            sys.stdout.write(message)
            sys.stdout.flush()


client_socket.close()
