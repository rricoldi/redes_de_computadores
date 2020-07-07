import socket
from threading import Thread

IP = input('Qual o endereço IP? ')  # Endereço IP
PORTA = int(input('Qual a porta que será escutada? '))      # Porta a ser escutada  

def conexao():  # Função para lidar com conexão de novos clientes
    while True:
        connection, address = server.accept()   # Aceitando um novo cliente e recebendo as informações deste
        lista_de_clientes.append(connection)    # Introdução do cliente à lista de clientes
        
        print('Conexão ativa com ', address)

        Thread(target=chat, args = (connection, address)).start()   # Nova thread para lidar com as mensagens do cliente conectado

def chat(connection, address):
    while True:
        mensagem = connection.recv(1024)    # Recebimento de uma mensagem
        
        if bytes("sair()", "utf8") in mensagem: # Casi receba a mensagem sair fechará a conexão e removerá o cliente da lista de clientes            
            print(address, " saiu do chat!")
            lista_de_clientes.remove(connection)
            connection.close()
            break

        for cliente in lista_de_clientes:   # Envia a mensagem a todos os clientes exceto quem enviou
            if cliente != connection: 
                try: 
                    cliente.send(mensagem)
                except: 
                    cliente.close()

    if lista_de_clientes.__len__() == 0:
        print('Não há clientes ativos!')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

server.bind((IP, PORTA))    # Atribui o ip e porta definidos ao socket
server.listen(PORTA)    # Socket começa a ouvir o endereço

lista_de_clientes = []

t = Thread(target=conexao())    # Thread principal
t.start()

server.close()  # Finaliza o socket