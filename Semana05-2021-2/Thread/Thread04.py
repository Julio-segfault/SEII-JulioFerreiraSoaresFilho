#Primeira versão apresentada no vídeo
#Programa que apenas dorme, com o propósito de simular uma espera por I/O
#Utiliza theads para executar o código de forma mais eficiente
#Essa versão é uma modificação de Thread03.py, aonde argumentos são passadas as funções executadas
#Especificamente quantos segundos a função deve esperar


#Importa a biblioteca com as funções de tempo
import time

#Importa biblioteca com as funções para programação com threads
import threading

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa
#Serve para simulação de I/O e fornece visualização do que está sendo executado ao usuário
#Agora aceita como argumento quantos segundos deve esperar
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(seconds)
    print(f'Done Sleeping...')

#Cria uma lista vazia que depois irá receber as threads criadas
#Isso é necessário pois o método join precisa ser realizado fora do loop
threads = []

#Utiliza um loop para criar 10 threads como objetos
#Além de no mesmo loop já começar a realizar o código
#A variável _ é uma variável descartável que serve apenas para realizar a contagem do loop
for _ in range(10):
    # Os argumentos são passados à função na criação do objeto com o parâmetro args do método Thread
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    #threads.append atribui as threads à lista
    threads.append(t)

#Esse loop é responsável por sincronizar todas as threads criadas com o programa principal
for thread in threads:
    thread.join()

#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')

#É possível perceber que com a utilização de threads é possível realizar a função do_something duas vezes
#em um segundo.