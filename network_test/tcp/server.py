import socket
import myconstants
import time
import math
from threading import Thread

#IP = input('Qual o endereço IP? ')  # Endereço IP
#PORTA = int(input('Qual a porta que será escutada? '))      # Porta a ser escutada  
IP = myconstants.IP
PORTA = myconstants.PORTA

def conexao():  # Função para lidar com conexão de novos clientes
	bytes_recebidos = 0
	pacotes = 0

	connection, address = server.accept()   # Aceitando um novo cliente e recebendo as informações deste        
	print('Conexão ativa com ', address)

	start = time.time()
	timeout = time.time() + myconstants.tempo_limite
	while time.time() < timeout:
		package = connection.recv(myconstants.tamanho_pacote)    # Recebimento de uma mensagem
		pacotes += 1
		bytes_recebidos += package.__len__()

	elapsed_time = time.time() - start
	velocidade = (bytes_recebidos/elapsed_time)/1000000
	print("pacotes   velocidade   tempo total\n------------------------------------------------\n{}       {} Mb/s      {} s".format(pacotes, velocidade, elapsed_time))

	connection.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

server.bind((IP, PORTA))    # Atribui o ip e porta definidos ao socket
server.listen(PORTA)    # Socket começa a ouvir o endereço

conexao()

server.close()  # Finaliza o socket