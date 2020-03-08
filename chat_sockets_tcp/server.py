import socket
from threading import Thread

IP = '127.0.0.1'  # Endereço IP
PORTA = 8080           # Porta a ser escutada

def conexao():
    while True:
        connection, address = server.accept()
        lista_de_clientes.append(connection)
        
        print('Conexão ativa com ', address)

        Thread(target=chat, args = (connection, address)).start()

def chat(connection, address):
    while True:
        mensagem = connection.recv(1024)
        
        if mensagem == bytes("sair()", "utf8"):            
            lista_de_clientes.remove(connection)
            connection.close()
            break
        
        mensagem = bytes('<' + address[0] + '> ', 'utf8') + mensagem

        for cliente in lista_de_clientes:
            if cliente != connection: 
                try: 
                    cliente.send(mensagem)
                except: 
                    cliente.close()

    if lista_de_clientes.__len__() == 0:
        print('Não há clientes ativos!')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, PORTA))
server.listen(PORTA)

lista_de_clientes = []

t = Thread(target=conexao())
t.start()

server.close()