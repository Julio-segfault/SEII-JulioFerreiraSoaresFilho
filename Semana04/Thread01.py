#Primeira versão apresentada no vídeo
#Programa que apenas dorme, com o propósito de simular uma espera por I/O


#Importa a biblioteca com as funções de tempo
import time

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa de 1 segundo
def do_something():
    print(f'Sleeping 1 second...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(1)
    print(f'Done Sleeping...')

#Executa a função
do_something()
do_something()


#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')