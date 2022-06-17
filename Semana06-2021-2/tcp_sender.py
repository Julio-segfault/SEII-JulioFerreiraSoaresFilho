import socket #biblioteca de socket
import sys #bibliotece do sistema

TCP_IP = "127.0.0.1" #Ip especial de referência à própria máquina
FILE_PORT = 5005 #porta do arquivos
DATA_PORT = 5006 #porta de dados
buf = 1024
file_name = sys.argv[1] #endereço do arquivo, passado na chamada do programa


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket ipv4 TCP
    sock.connect((TCP_IP, FILE_PORT)) # conecta com a porta de arquivos
    sock.send(file_name) # envia arquivo
    sock.close() #fecha socket

    print ("Sending %s ..." % file_name) #imprime status

    f = open(file_name, "rb") #abre o arquivo
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria socket ipv4 TCP
    sock.connect((TCP_IP, DATA_PORT)) # conexão com a porta de dados
    data = f.read() # lê o arquivo aberto para a variável data
    sock.send(data) #envia data via socket

finally: # após bloco try
    sock.close() #fecha o socket
    f.close() #fecha o arquivo