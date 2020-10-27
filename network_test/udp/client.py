import socket
import sys
import myconstants
import math
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
inicio = time.time()

try:
	sent = sock.sendto(bytes(str(myconstants.tamanho_pacote), "utf8"), server_address)
	sent = sock.sendto(bytes(str(myconstants.num_pacotes_por_vez), "utf8"), server_address)
	contador_pacotes = 1

	##########################################################################################################
	#### UPLOAD # UDP ########################################################################################
	##########################################################################################################
	
	while time.time() - inicio < 20:
		try:
			for i in range(myconstants.num_pacotes_por_vez):
				message_contador = bytes('{:0>1000}'.format(format(contador_pacotes, 'x')), 'utf8') #
				sock.sendto(message_contador, server_address)
				contador_pacotes += 1
		except TimeoutError:
			contador_pacotes -= myconstants.num_pacotes_por_vez

	send_finalizado = bytes('{:0>{}}'.format('1234567891000000', myconstants.tamanho_bytes), 'utf8')
	for i in range(5):
		sock.sendto(send_finalizado, server_address)
		time.sleep(0.1)
	data, address = sock.recvfrom(4096)
	pacotes_recebidos = int(data.decode('utf8'))
	print('pacotes   velocidade   tempo total   pacotes perdidos  \n------------------------------------------------\n{}       {} Mb/s      {:.2f} s    {}   <==>  UPLOAD'.format(str(contador_pacotes), str(math.ceil(((contador_pacotes*myconstants.tamanho_pacote*8/(1024*1024))/(time.time() - inicio)))), time.time() - inicio, str(contador_pacotes-pacotes_recebidos)))

	##########################################################################################################
	#### UPLOAD # TCP ########################################################################################
	##########################################################################################################
	
	num_pacotes = 0
	inicio = time.time()

	while time.time() - inicio < 20:
		contador = 0
		while(contador < myconstants.num_pacotes_por_vez):
			time.time() - inicio > 20
			data, address = sock.recvfrom(4096)
			num_pacotes = num_pacotes + 1
			contador = contador + 1

	for i in range(5):
		sock.sendto(send_finalizado, server_address)
		time.sleep(0.1)

	while True:
		if '1234567891000000' in str(data[:16]):
			data, address = sock.recvfrom(4096)
			if '1234567891000000' in str(data[:16]):
				data, address = sock.recvfrom(4096)
			if '1234567891000000' in str(data[:16]):
				data, address = sock.recvfrom(4096)
			if '1234567891000000' in str(data[:16]):
				data, address = sock.recvfrom(4096)
			if '1234567891000000' in str(data[:16]):
				data, address = sock.recvfrom(4096)
			pacotes_totais = int(data.decode('utf8'))
			break
		data, address = sock.recvfrom(4096)
	
	print('------------------------------------------------\n{}       {} Mb/s      {:.2f} s    {}   <==>  DOWNLOAD'.format(str(pacotes_totais), str(math.ceil(((num_pacotes*myconstants.tamanho_pacote*8/(1024*1024))/20.5))), 20.50, str(pacotes_totais-num_pacotes)))
finally:
    sock.close()

