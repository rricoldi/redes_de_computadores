import socket
from threading import Thread

HOST = '127.0.0.1'  # Endereço IP
PORT = 8080           # Porta a ser escutada

def receber():
    while True:
        try:
            mensagem = server.recv(1024).decode("utf8")
            print(mensagem)
        except OSError:
            break


def enviar():
  while True:
    mensagem = input()

    server.send(bytes(mensagem, "utf8"))
    if mensagem == "sair()":
      server.close()
      break
      

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

print('Para sair use a função sair()\n')

Thread(target=receber).start()
Thread(target=enviar).start()
