import socket
import datetime
import sys
from threading import Thread

HOST = input('Qual o endereço IP? ')  # Endereço IP que tentará conectar
PORTA = int(input('Qual a porta que será conectada? '))      # Porta a ser conectada
nome = input('Digite o nome que será usado no chat: ')

def receber():  # Função que recebe as mensagens do servidor e mostra ao cliente
    while True:
        try:
            mensagem = server.recv(1024).decode("utf8")
            print(mensagem)
        except OSError:
            break


def enviar(): # Função que recebe mensagens do cliente e as envia ao servidor
  while True:
    mensagem = sys.stdin.readline() 
    x = datetime.datetime.now()
    mensagem = "[" + x.strftime("%H") + ":" + x.strftime("%M") + "] " + nome + " > " + mensagem

    server.send(bytes(mensagem, "utf8"))
    
    if "sair()" in mensagem:  # Caso a mensagem seja "sair()" fecha a conexão
      server.close()
      break
      

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket
server.connect((HOST, PORTA))  # Conecta ao servidor

print('Para sair use a função sair()\n')

Thread(target=receber).start()  # Threads para receber e enviar ao mesmo tempo
Thread(target=enviar).start()
