import socket
from threading import Thread

HOST = '127.0.0.1'  # Endereço IP
PORT = 8080           # Porta a ser escutada

def client():
    print('<' + address[0] + '>')
    message = connection.recv(1024).decode('utf-8', 'strict')
    if not message:
        print('Conexão finalizada!')
        connection.close()
    print(' - ' + message)

def server_messages():
    print('<You>')
    message = input()
    if message != 'exit()':
        connection.send(message.encode('utf-8', 'strict'))
    return

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do socket

server.bind((HOST, PORT))   # Associa ao endereço e à porta designada
server.listen() # Servidor escutando na porta

while True:
    connection, address = server.accept()
    print('Conexão ativa com ', address)
    break

t1 = Thread(target=client())
t2 = Thread(target=server_messages())
t1.start()
t2.start()
t1.join()
t2.join()
