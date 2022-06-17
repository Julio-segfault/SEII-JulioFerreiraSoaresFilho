import socket # importa biblioteca de socket

HEADER = 64 #define tamanho da mensagem
PORT = 5050 #define a porta para envio
SERVER = "192.168.1.35" #endereço ip do servidor
ADDR = (SERVER, PORT) #endereço do servidor( ip + porta)
FORMAT = 'utf-8' #formato da mensagem
DISCONNECT_MESSAGE = "!Disconnect" #mensagem para término de conexão

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#cria um objeto socket para o cliente. Ipv4, TCP
client.connect(ADDR) #connecta o cliente ao servidor

def send(msg): #função para o envio de mensagens
    message = msg.encode(FORMAT) #codifica a mensagem no formato de envio
    msg_length = len(message) #obtém o tamanho da mensagem
    send_length = str(msg_length).encode(FORMAT) #codifica a informação do tamanho da mensagem
    send_length += b' ' * (HEADER - len(send_length)) #faz o padding da mensagem com o tamanho
    client.send(send_length) #envio o tamanho da mensagem a ser recebida
    client.send(message) #envia a mensagem
    print(client.recv(2048).decode(FORMAT)) #imprime a resposta do servidor

send("Hello World!") #mensagem 1
input() #Espera teclado
send("Hello Everyone!") #mensagem 2
input() #Espera teclado
send("Hello Tim!") #mensagem 3

send(DISCONNECT_MESSAGE) #finaliza conexão