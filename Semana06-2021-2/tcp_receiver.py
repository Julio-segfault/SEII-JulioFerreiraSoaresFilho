import socket #biblioteca de socket

TCP_IP = "127.0.0.1" #Ip especial local
FILE_PORT = 5005 #porta de arquivos
DATA_PORT = 5006 #porta de dados
timeout = 3
buf = 1024 #tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket de arquivos ipv4 TCP
sock_f.bind((TCP_IP, FILE_PORT)) #faz o bind na porta de arquivos
sock_f.listen(1) #Escuta na porta, argumento especifica o número de conexões

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria socket de dados ipv4 TCP
sock_d.bind((TCP_IP, DATA_PORT)) #faz o bind na porta de dados
sock_d.listen(1) #Escuta na porta, argumento especifica o número de conexões


while True: #loop infinito para aceitar conexões no socket de arquivo
    conn, addr = sock_f.accept() #aceita conexão
    data = conn.recv(buf) #recebe dados
    if data: #condicional se dados foram recebidos
        print ("File name:", data) #Exibe o nome do arquivo
        file_name = data.strip() # remove espaços

    f = open(file_name, 'wb') #abre um arquivo para escrita

    conn, addr = sock_d.accept() #aceita conexão
    while True: #loop infinito para aceitar conexões no socket de dados
        data = conn.recv(buf) #recebe dados
        if not data: # se vazio sai do loop
            break
        f.write(data) #escreve no arquivo os dados recebidos

    print ("%s Finish!" % file_name) #imprime que o processo terminou
    f.close() #fecha o arquivo