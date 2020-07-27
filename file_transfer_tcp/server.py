import socket
import myconstants
from threading import Thread

IP = input('Qual o endereço IP? ')  # Endereço IP
PORTA = int(input('Qual a porta que será escutada? '))      # Porta a ser escutada  


def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def conexao():  # Função para lidar com conexão de novos clientes
    file_size = 0
    package_counter = 0
    while True:
        connection, address = server.accept()   # Aceitando um novo cliente e recebendo as informações deste        
        print('Conexão ativa com ', address)

        while True:
            package = connection.recv(myconstants.tamanho_pacote)    # Recebimento de uma mensagem
            if bytes("sair", "utf8") in package:
                connection.send(bytes('finalizado, tamanho: ' + str(file_size) + ' B, ' + str(package_counter) + ' pacotes recebidos.', "utf8"))
                break
            package_counter = bytes_to_int(package[0:4])
            file_size = file_size + package.__len__()
            lista_de_pacotes.append((package_counter, package[5:package.__len__()-1]))
            connection.send(bytes('recebido', "utf8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket

server.bind((IP, PORTA))    # Atribui o ip e porta definidos ao socket
server.listen(PORTA)    # Socket começa a ouvir o endereço

lista_de_pacotes = []

t = Thread(target=conexao())    # Thread principal
t.start()

server.close()  # Finaliza o socket