import socket
from threading import Thread

HOST = '127.0.0.1'  # Endereço IP
PORT = 8080           # Porta a ser escutada

def receber():  # Função que recebe as mensagens do servidor e mostra ao cliente
    while True:
        try:
            mensagem = server.recv(1024).decode("utf8")
            print(mensagem)
        except OSError:
            break


def enviar(): # Função que recebe mensagens do cliente e as envia ao servidor
  while True:
    mensagem = input()

    server.send(bytes(mensagem, "utf8"))
    if mensagem == "sair()":  # Caso a mensagem seja "sair()" fecha a conexão
      server.close()
      break
      

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
server.connect((HOST, PORT))  # Conecta ao servidor

print('Para sair use a função sair()\n')

Thread(target=receber).start()  # Threads para receber e enviar ao mesmo tempo
Thread(target=enviar).start()
