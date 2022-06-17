import socket #biblioteca de socket
import time #biblioteca com as funções referentes à contagem de tempo
import sys #biblioteca com funções de sistema

UDP_IP = "127.0.0.1" #Ip especial local
UDP_PORT = 5005 #Porta UDP
buf = 1024 #tamanho do buffer
file_name = sys.argv[1] #recebe o endereço do arquivo como argumento


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria socket ipv4 UDP
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #Envia nome da arquivo
print ("Sending %s ..." % file_name) #Imprime status

f = open(file_name, "r") #Abre o arquivo
data = f.read(buf) #Lê uma parte do arquivo
while(data): #Enquanto ainda houver dados a serem lidos no arquivo
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #Envia dados do arquivo
        data = f.read(buf) #Lê a próxima parte do arquivo
        time.sleep(0.02) # Tempo entre envios (para garantir recebimento e processamento no servidor)

sock.close() #Fecha socket
f.close() #Fecha arquivo