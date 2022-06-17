import socket #biblioteca socket
import select #biblioteca para espera de I/O

UDP_IP = "127.0.0.1" #Ip especial local
IN_PORT = 5005 #Porta do servidor
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria socket ipv4 UDP
sock.bind((UDP_IP, IN_PORT)) #Faz o bind no IP e porta

while True: #loop infinito de escuta
    data, addr = sock.recvfrom(1024) #recebe dados
    if data: #Se dados são recebidos
        print ("File name:", data) #Exibe nome do arquivo
        file_name = data.strip() #Retira espaços

    f = open(file_name, 'wb') #Abre um arquivo para escrita

    while True: #Loop infinito para recebimento dos dados
        ready = select.select([sock], [], [], timeout) #Espera até o socket estar pronta pra ler por timeout segundos
        if ready[0]:
            data, addr = sock.recvfrom(1024) #Recebe dados do arquivo
            f.write(data) #Escreve os dados no arquivo aberto
        else:
            print ("%s Finish!" % file_name)
            f.close() #Fecha arquivo
            break # Sai do loop