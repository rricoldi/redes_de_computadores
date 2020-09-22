import socket
import sys

lista_de_pacotes = dict({})

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

data, address = sock.recvfrom(4096)
nome_arquivo = data.decode('utf8')

data, address = sock.recvfrom(4096)
max_pacote = int(data.decode('utf8'))
print('máximo de pacotes: {}'.format(max_pacote))
data, address = sock.recvfrom(4096)

tamanho_do_pacote = int(data.decode('utf8'))
print('tamanho de cada pacote: {}'.format(tamanho_do_pacote))

num_pacotes = 0

while num_pacotes < max_pacote:
    data, address = sock.recvfrom(tamanho_do_pacote+20)

    print('received {} bytes from {}'.format(
        len(data), address))
    
    lista_de_pacotes[int(str(data)[2:18])] = data[16:]
    
    num_pacotes = num_pacotes + 1




arquivo = open("downloaded-{}".format(nome_arquivo), "wb+")
contador_pacotes = 0
for contador_pacotes in lista_de_pacotes:
    arquivo.write(lista_de_pacotes[contador_pacotes])

    # if data:
    #     sent = sock.sendto(data, address)
    #     print('sent {} bytes back to {}'.format(
    #         sent, address))