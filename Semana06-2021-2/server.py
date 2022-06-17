import socket #biblioteca com as funções de socket
import threading #biblioteca com as funções de threading
#import time

HEADER = 64 #tamanho da mensagem
PORT = 5050 #endereço da porta do servidor
#SERVER = "192.168.1.35" #designa um ip para o server na rede local
SERVER = socket.gethostbyname(socket.gethostname()) #utiliza a biblioteca socket para adquirir o endereço ip
ADDR = (SERVER, PORT) #endereço do servidor (ip e porta)
FORMAT = 'utf-8' #formato da transmissão de dados
DISCONNECT_MESSAGE = "!Disconnect" #mensagem de fim de conexão

print(socket.gethostname()) #exibe o ip

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#inicializa o objeto server com as funções da biblioteca de socket
#socket.AF_INET especifica o tipo de socket (ipv4), socket.sock_stream especifica o protocolo de transmissão (TCP)

server.bind(ADDR) #Realiza o bind do servidor no endereço

def handle_client(conn, addr) : #função que lida com as conexões e comunicações dos clientes
    print (f"[NEW CONNECTION] {addr} connected.") #Exibe a que um novo endereço começou uma conexão

    connected = True #flag que determina se a conexão está ativa
    while connected: #loop que mantém a conexão
        msg_length = conn.recv(HEADER).decode(FORMAT) #recebe e decodifica o tamanho da mensagem a ser recebida.
        msg_length = int(msg_length) #type casting
        msg = conn.recv(HEADER).decode(FORMAT) #recebe e decodifica a mensagem
        if msg == DISCONNECT_MESSAGE: #condição para término da conexão
            connected = False #Alternativamente break
        print(f"[{addr}] {msg}") #Exibe o endereço de envio e a mensagem
        conn.send("Msg received".encode(FORMAT)) #Envia a confirmação de recebimento para o remetente
    conn.close() #finaliza conexão

def start (): #função que inicializa o servidor
    server.listen() #servidor escuta na porta
    print(f"[LISTENING] Server is listening on {SERVER}") #Exibe que o servidor está ativo
    while True: #loop infinito de escuta
        conn, addr = server.accept() #recebe o endereço do cliente
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        #constrói um objeto thread com a função handle client e os argumentos da conexão
        thread.start() #inicializa a thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") #Exibe quantas conexões estão ativas


print("[STARTING] server is starting ...") #mensagem de início do servidor
start() #inicializa servidor