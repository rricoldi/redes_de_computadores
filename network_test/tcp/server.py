import socket
import myconstants
import time
import random
import math
from threading import Thread

IP = myconstants.IP
PORTA = myconstants.PORTA

def receber(connection):
	timeout = time.time() + myconstants.tempo_limite

	while time.time() < timeout:
		connection.recv(myconstants.tamanho_pacote)
		connection.send(bytes('1', 'utf8'))

def enviar(connection):
	timeout = time.time() + myconstants.tempo_limite

	while time.time() < timeout:
		mensagem = bytes(bin(random.getrandbits(myconstants.tamanho_pacote)), 'utf8')
		connection.send(mensagem)

def conexao():
	connection, address = server.accept()
	print('starting up on port {}'.format(address))

	connection.send(bytes('upload', 'utf8'))
	print('iniciando upload')
	receber(connection)
	connection.send(bytes('fim-upload', 'utf8'))

	time.sleep(0.1)

	connection.send(bytes('download', 'utf8'))
	print('iniciando download')
	enviar(connection)
	connection.send(bytes('fim-download', 'utf8'))

	fim = connection.recv(5).decode('utf8')
	if not 'fim' in fim:
		time.sleep(1)

	connection.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

server.bind((IP, PORTA))    # Atribui o ip e porta definidos ao socket
server.listen(PORTA)    # Socket começa a ouvir o endereço

random.seed()
conexao()

server.close()  # Finaliza o socket