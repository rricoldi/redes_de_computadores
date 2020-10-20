import socket
import math
import sys
import myconstants
import time
import random
from threading import Thread

HOST = myconstants.IP
PORTA = myconstants.PORTA

def enviar(): # Função que recebe mensagens do cliente e as envia ao servidor
	timeout = time.time() + myconstants.tempo_limite

	while time.time() < timeout:
		mensagem = bytes(bin(random.getrandbits(myconstants.tamanho_pacote)))
		server.send(mensagem)
	#	cont_bin = "{:0>16}".format(str(contador_pacotes))
	#	bytes_lidos = bytes(arquivo.read(myconstants.tamanho_pacote - myconstants.tamanho_bytes))
	#	mensagem = b"".join([bytes(cont_bin[-myconstants.tamanho_bytes:], "utf8"), bytes_lidos])
	#	server.send(mensagem)
	#	contador_pacotes += 1 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
server.connect((HOST, PORTA))  # Conecta ao servidor

random.seed()
enviar()