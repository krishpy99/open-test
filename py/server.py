import socket
import threading
import sys

server_socket = socket.socket()

IP = str(sys.argv[1])

Port = int(sys.argv[2])

server_socket.bind((IP, Port))

server_socket.listen(100)

client_list = []


def clientThread(conn, addr):
    conn.send("Sample Chatroom!")
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + ">: " + message)
                message_to_send = "<" + addr[0] + ">: " + message
                broadcast(message_to_send, conn)

            else:
                remove(conn)

        except Exception as ex:
            print(ex)
            continue


def broadcast(message, connection):
    for client in client_list:
        if client != connection:
            try:
                client.send(message)
            except Exception as ex:
                print(ex)
                client.close()

                remove(client)


def remove(conn):
    if conn in client_list:
        client_list.remove(conn)


while True:
    conn, addr = server_socket.accept()

    client_list.append(conn)

    print(addr[0] + " connected")

    threading.Thread(clientThread, (conn, addr)).start()


conn.close()
server_socket.close()
