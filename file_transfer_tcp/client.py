import socket
import math
import sys
import myconstants
import time
from threading import Thread

HOST = myconstants.IP
PORTA = myconstants.PORTA

def receber():  # Função que recebe as mensagens do servidor e mostra ao cliente
	while True:
		try:
			mensagem = server.recv(1024).decode('utf8')
			if 'finalizado' in mensagem:
				print(mensagem)
				break

		except OSError:
			break


def enviar(): # Função que recebe mensagens do cliente e as envia ao servidor
	nome_arquivo = input('Digite o nome do arquivo a ser enviado: ')
	arquivo = open(nome_arquivo, "rb")
	arquivo.seek(0, 2)				#vai para o fim do arquivo
	tamanho_arquivo = arquivo.tell()
	arquivo.seek(0)					#retorna o file pointer para o início

	quantidade_pacotes = math.ceil(tamanho_arquivo/(myconstants.tamanho_pacote - myconstants.tamanho_bytes))
	contador_pacotes = 0			#incrementa com cada pacote enviado
	if quantidade_pacotes > myconstants.limite_pacotes:
		print("Error: file is overwhelmingly large")
		return

	#envia um pacote que espicifica quantos pacotes a mais virão
	primeiro = "{:0>16}".format(quantidade_pacotes)
	server.send(bytes(primeiro, "utf8"))

	while contador_pacotes < quantidade_pacotes:
		cont_bin = "{:0>16}".format(str(contador_pacotes))
		bytes_lidos = bytes(arquivo.read(myconstants.tamanho_pacote - myconstants.tamanho_bytes))
		mensagem = b"".join([bytes(cont_bin[-myconstants.tamanho_bytes:], "utf8"), bytes_lidos])
		server.send(mensagem)
		contador_pacotes += 1 

	arquivo.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
server.connect((HOST, PORTA))  # Conecta ao servidor

#opcao = input('Envie a palavra AMOR para 4002-8922 e receba dicas diárias no seu celular')
#if opcao == 'enviar':
t = Thread(target=enviar)  # Threads para receber e enviar ao mesmo tempo
Thread(target=receber).start()
t.start()
t.join()
#else:
