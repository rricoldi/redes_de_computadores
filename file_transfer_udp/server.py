import socket
import sys


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

data, address = sock.recvfrom(4096)
tamanho = int(data.decode('utf8'))
print('tamanho do arquivo: {}'.format(tamanho))
data, address = sock.recvfrom(4096)

tamanho_do_pacote = int(data.decode('utf8'))
print('tamanho do pacote: {}'.format(tamanho_do_pacote))

bytes_lidos = 0

while bytes_lidos < tamanho:
    data, address = sock.recvfrom(tamanho_do_pacote)

    print('received {} bytes from {}'.format(
        len(data), address))
        
    bytes_lidos = bytes_lidos + tamanho_do_pacote


    # if data:
    #     sent = sock.sendto(data, address)
    #     print('sent {} bytes back to {}'.format(
    #         sent, address))