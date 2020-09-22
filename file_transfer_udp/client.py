import socket
import sys
import myconstants
import math

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
	sent = sock.sendto(bytes(str(tamanho_arquivo), "utf8"), server_address)
	sent = sock.sendto(bytes(str(myconstants.tamanho_pacote), "utf8"), server_address)
	# Send data
	max_pacotes = math.ceil(tamanho_arquivo/(myconstants.tamanho_pacote - myconstants.tamanho_bytes))
	contador_pacotes = 0

	while max_pacotes > contador_pacotes:
		bytes_lidos = arquivo.read(myconstants.tamanho_pacote - myconstants.tamanho_bytes)
		message = "{:0>16}".format(format(contador_pacotes, 'b'))
		message = bytes(message + bytes_lidos, 'utf8')
		sock.sendto(message, server_address)
		contador_pacotes += 1

    # Receive response
    # print('waiting to receive')
    # data, server = sock.recvfrom(4096)
    # print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
