import socket
import sys
import myconstants
import math
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
# message = b'This is the message.  It will be repeated.'
nome_arquivo = input('Digite o nome do arquivo a ser enviado: ')
arquivo = open(nome_arquivo, "rb")
arquivo.seek(0, 2)				#vai para o fim do arquivo
tamanho_arquivo = arquivo.tell()
arquivo.seek(0)
try:
	max_pacotes = math.ceil(tamanho_arquivo/(myconstants.tamanho_pacote - myconstants.tamanho_bytes))
	sent = sock.sendto(bytes(nome_arquivo, "utf8"), server_address)
	sent = sock.sendto(bytes(str(max_pacotes), "utf8"), server_address)
	sent = sock.sendto(bytes(str(myconstants.tamanho_pacote), "utf8"), server_address)
	print(max_pacotes)
	# Send data
	contador_pacotes = 1

	while max_pacotes > contador_pacotes-1:
		print(format(contador_pacotes, 'x'))

		bytes_lidos = arquivo.read(myconstants.tamanho_pacote - myconstants.tamanho_bytes)
		message_contador = bytes('{:0>{}}'.format(format(contador_pacotes, 'x'), myconstants.tamanho_bytes), 'utf8')
		message = b"".join([message_contador, bytes_lidos])
		sock.sendto(message, server_address)
		contador_pacotes += 1
		#time.sleep(0.00005)
	print("pacotes enviados: ", max_pacotes)

	send_finalizado = bytes('{:0>{}}'.format('0', myconstants.tamanho_bytes), 'utf8')
	for i in range(5):
		print('sending null message, attempt ', i)
		sock.sendto(send_finalizado, server_address)
		time.sleep(0.1)


finally:
    print('closing socket')
    sock.close()
