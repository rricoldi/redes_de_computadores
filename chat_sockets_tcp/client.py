import socket

HOST = '127.0.0.1'  # Endereço IP
PORT = 8080           # Porta a ser escutada

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

print('Para sair use a função exit()\n')

message = input()

while message != 'exit()':
    server.send(message.encode('utf-8', 'strict'))
    message = input()

server.close()