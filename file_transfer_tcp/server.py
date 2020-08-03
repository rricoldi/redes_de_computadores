import socket
import myconstants
import time
import math
from threading import Thread

#IP = input('Qual o endereço IP? ')  # Endereço IP
#PORTA = int(input('Qual a porta que será escutada? '))      # Porta a ser escutada  
IP = myconstants.IP
PORTA = myconstants.PORTA

def bytes_to_int(bytes):
	result = 0
	for b in bytes:
		result = result * 256 + int(b)
	return result

def atoi(str):
	result = 0
	for b in str:
		result = result * 10 + int(b) - 48
	return result

def conexao():  # Função para lidar com conexão de novos clientes
	file_size = 0
	package_counter = 0
	max_pacotes = 0
	sair = False
	while not(sair):
		connection, address = server.accept()   # Aceitando um novo cliente e recebendo as informações deste        
		print('Conexão ativa com ', address)

		start = time.time()
		while not(sair):
			package = connection.recv(myconstants.tamanho_pacote)    # Recebimento de uma mensagem
			if bytes("sair", "utf8") in package:
				sair = True
				response = 'finalizado\ntamanho   pacotes   velocidade   tempo total  \n------------------------------------------------\n{:.2f} MB  {}   {} b/s   {:.2f} s'.format(file_size/(1024*1024), str(lista_de_pacotes.__len__()), str(math.ceil((file_size*8)/(time.time() - start - myconstants.tempo))), time.time() - start - myconstants.tempo) 
				
				connection.send(bytes(response, "utf8"))
				break
			package_counter = atoi(package[0:myconstants.tamanho_bytes])
			max_pacotes += 1
			file_size = file_size + package.__len__() - myconstants.tamanho_bytes
			lista_de_pacotes.append((package_counter, package[myconstants.tamanho_bytes:package.__len__()]))
		connection.close()
	#arquivo = open("download.rar", "wb+")
	#contador_pacotes = 0
	#while True:
	#	for x in lista_de_pacotes:
	#		if contador_pacotes == x[0]:
	#			contador_pacotes += 1
	#			arquivo.write(x[1])
	#	if contador_pacotes >= max_pacotes:
	#		break
	#arquivo.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

server.bind((IP, PORTA))    # Atribui o ip e porta definidos ao socket
server.listen(PORTA)    # Socket começa a ouvir o endereço

lista_de_pacotes = []

t = Thread(target=conexao())    # Thread principal
t.start()

server.close()  # Finaliza o socket