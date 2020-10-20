import socket
import sys
import myconstants
import math
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
# message = b'This is the message.  It will be repeated.'
nome_arquivo = 'teste.03.520MB.rar'
arquivo = open(nome_arquivo, "rb")
# arquivo.seek(0, 2)				#vai para o fim do arquivo
# tamanho_arquivo = arquivo.tell()
# arquivo.seek(0)

inicio = time.time()

try:
	# max_pacotes = math.ceil(tamanho_arquivo/(myconstants.tamanho_pacote - myconstants.tamanho_bytes))
	# sent = sock.sendto(bytes(nome_arquivo, "utf8"), server_address)
	# sent = sock.sendto(bytes(str(max_pacotes), "utf8"), server_address)
	sent = sock.sendto(bytes(str(myconstants.tamanho_pacote), "utf8"), server_address)
	sent = sock.sendto(bytes(str(myconstants.num_pacotes_por_vez), "utf8"), server_address)
	# print(max_pacotes)
	# Send data
	contador_pacotes = 1

	# while max_pacotes > contador_pacotes-1:
	while time.time() - inicio < 20:
		try:
			for i in range(myconstants.num_pacotes_por_vez):

				bytes_lidos = arquivo.read(myconstants.tamanho_pacote - myconstants.tamanho_bytes)
				message_contador = bytes('{:0>16}'.format(format(contador_pacotes, 'x')), 'utf8') #
				message = b"".join([message_contador, bytes_lidos])
				# print("{}   {}    {}\n".format(message, message_contador, bytes_lidos))
				sock.sendto(message, server_address)
				contador_pacotes += 1
		except TimeoutError:
			contador_pacotes -= myconstants.num_pacotes_por_vez

		#time.sleep(0.00005)
	# print("pacotes enviados: {}".format(contador_pacotes))

	send_finalizado = bytes('{:0>{}}'.format('0', myconstants.tamanho_bytes), 'utf8')
	for i in range(5):
		# print('sending null message, attempt ', i)
		sock.sendto(send_finalizado, server_address)
		time.sleep(0.1)


finally:
    # print('closing socket')
    sock.close()

print('finalizado upload\n\npacotes   velocidade   tempo total  \n------------------------------------------------\n{}       {} Mb/s      {:.2f} s'.format(str(contador_pacotes), str(math.ceil(((contador_pacotes*484*8/(1024*1024))/(time.time() - inicio)))), time.time() - inicio))
