import socket
import myconstants
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

data, address = sock.recvfrom(4096)
num_pacotes_por_vez = int(data.decode('utf8'))

num_pacotes = 1

arquivo = open("downloaded-{}".format(nome_arquivo), "wb+")

while True:
    contador = 0
    while(contador < num_pacotes_por_vez):
        data, address = sock.recvfrom(1016)

        if '0000000000000000' in str(data[:16]):
            print('null message received, breaking')
            break
        lista_de_pacotes[int(str(data)[2:myconstants.tamanho_bytes+2], 16)] = data[myconstants.tamanho_bytes:]
        contador = contador + 1

    if '0000000000000000' in str(data[:16]):
        print('null message received, breaking')
        break
    
    contador_pacotes = int(str(data)[2:myconstants.tamanho_bytes+2], 16) - num_pacotes_por_vez
    while True:
        escritos = arquivo.write(lista_de_pacotes[contador_pacotes + 1])
        contador_pacotes = contador_pacotes + 1
        if(contador_pacotes == int(str(data)[2:myconstants.tamanho_bytes+2], 16)):
            lista_de_pacotes.clear()
            break


    sock.sendto(bytes('Recebido', 'utf8 '), address)

    # print('{}, pacotes: {}'.format(str(data[:16]), num_pacotes))


    num_pacotes = num_pacotes + num_pacotes_por_vez
    if num_pacotes-1 >= max_pacote:
        print('all packets received, breaking')
        break




# arquivo = open("downloaded{}".format(nome_arquivo[-4:]), "wb+")
    # contador_pacotes = 0
    # for contador_pacotes in lista_de_pacotes:
    #     escritos = arquivo.write(lista_de_pacotes[contador_pacotes])

    #     # if data:
    #     #     sent = sock.sendto(data, address)
    #     #     print('sent {} bytes back to {}'.format(
    #     #         sent, address))