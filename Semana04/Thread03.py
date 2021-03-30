#Primeira versão apresentada no vídeo
#Programa que apenas dorme, com o propósito de simular uma espera por I/O
#Utiliza theads para executar o código de forma mais eficiente
#Nessa versão são criadas várias threads com um loop para melhor comparar a diferença de desempenho
#Com e sem threads


#Importa a biblioteca com as funções de tempo
import time

#Importa biblioteca com as funções para programação com threads
import threading

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa de 1 segundo
#Serve para simulação de I/O e fornece visualização do que está sendo executado ao usuário
def do_something():
    print(f'Sleeping 1 second...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(1)
    print(f'Done Sleeping...')

#Cria uma lista vazia que depois irá receber as threads criadas
#Isso é necessário pois o método join precisa ser realizado fora do loop
threads = []

#Utiliza um loop para criar 10 threads como objetos
#Além de no mesmo loop já começar a realizar o código
#A variável _ é uma variável descartável que serve apenas para realizar a contagem do loop
for _ in range(10):
    t = threading.Thread(target=do_something)
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

#É possível perceber que com a utilização de threads é possível realizar a função do_something dez vezes
#em um segundo.