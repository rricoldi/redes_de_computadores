import socket
import math
import sys
import myconstants
import time
import random
from threading import Thread

HOST = myconstants.IP
PORTA = myconstants.PORTA

def upload():
	bytes_recebidos = 0
	pacotes = 0

	start = time.time()
	while True:
		try:
			mensagem = bytes(bin(random.getrandbits(myconstants.tamanho_pacote)), 'utf8')
			bytes_recebidos += server.send(mensagem)
			pacotes += 1
			mensagem = server.recv(20).decode('utf8')
			if 'fim-upload' in mensagem:
				break
		except TimeoutError:
			break

	elapsed_time = time.time() - start
	velocidade = (bytes_recebidos*8/elapsed_time) / 1000000
	pacotes_seg = math.ceil(pacotes/elapsed_time)
	print(
		"pacotes/s    bytes recebidos     velocidade     tempo total\n------------------------------------------------\n{}          {}        {:.2f} Mb/s       {:.2f} s       <==>  UPLOAD".format(
		pacotes_seg, bytes_recebidos, velocidade, elapsed_time))

def download():
	bytes_enviados = 0
	pacotes = 0

	start = time.time()
	while True:
		try:
			mensagem = server.recv(myconstants.tamanho_pacote)
			mensagem = mensagem.decode('utf8')
			bytes_enviados += mensagem.__len__()
			pacotes += 1
			if 'fim-download' in mensagem:
				break
		except TimeoutError:
			break

	elapsed_time = time.time() - start
	velocidade = (bytes_enviados * 8 / elapsed_time) / 1000000
	pacotes_seg = math.ceil(pacotes / elapsed_time)
	print(
		"------------------------------------------------\n{}          {}        {:.2f} Mb/s       {:.2f} s       <==>  DOWNLOAD".format(
			pacotes_seg, bytes_enviados, velocidade, elapsed_time))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
server.connect((HOST, PORTA))  # Conecta ao servidor

random.seed()

mensagem = server.recv(4096)
mensagem = mensagem.decode('utf8')
if 'upload' in mensagem:
	upload()

time.sleep(0.1)

mensagem = server.recv(4096)
mensagem = mensagem.decode('utf8')
if 'download' in mensagem:
	download()

server.send(bytes('fim', 'utf8'))
