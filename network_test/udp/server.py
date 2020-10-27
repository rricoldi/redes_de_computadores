import socket
import myconstants
import time
import sys

lista_de_pacotes = dict({})

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

data, address = sock.recvfrom(4096)
tamanho_do_pacote = int(data.decode('utf8'))
print('tamanho de cada pacote: {}'.format(tamanho_do_pacote))

data, address = sock.recvfrom(4096)
num_pacotes_por_vez = int(data.decode('utf8'))

num_pacotes = 0


while True:
    contador = 0
    while(contador < num_pacotes_por_vez):
        data, address = sock.recvfrom(1016)
        
        if '1234567891000000' in str(data[:16]):
            print('Received {} packages'.format(num_pacotes))
            break
        num_pacotes = num_pacotes + 1
        contador = contador + 1

    if '1234567891000000' in str(data[:16]):
        sock.sendto(bytes('{}'.format(num_pacotes), 'utf8 '), address)
        break

contador_pacotes = 0
inicio = time.time()

try:
    while time.time() - inicio < 21:
        message_contador = bytes('{:0>1000}'.format(format(1243, 'x')), 'utf8')
        sock.sendto(message_contador, address)
        contador_pacotes += 1
    
    while True:
        data, address = sock.recvfrom(4096)
        if '1234567891000000' in str(data[:16]):
            for i in range(5):
                sock.sendto(bytes('{:0>{}}'.format('1234567891000000', 16), 'utf8'), address)
                time.sleep(0.1)
            sock.sendto(bytes('{}'.format(contador_pacotes), 'utf8 '), address)
            break
except TimeoutError:
    contador_pacotes -= num_pacotes_por_vez
    
