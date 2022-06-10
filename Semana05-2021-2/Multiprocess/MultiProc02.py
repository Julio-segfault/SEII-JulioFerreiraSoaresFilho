#Programa que cria vários processos filhos para executar uma função que simula uma operação (I/O ou execução_
#É utilizado um loop para criação dos processos, similar à Thread03.py, além do processo filho aceitar argumentos
#Como em Thread04.py


#Importa a biblioteca para multiprocessamento
import multiprocessing

#Importa a biblioteca com as funções de tempo
import time

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa
#Simula uma operação de I/O ou execução de código
#Agora aceita como argumento quantos segundos deve esperar
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(seconds)
    print(f'Done Sleeping...')

#Cria lista vazia para receber os processos durante o loop de criação
#E depois para realizar sincronização com o .join
processes = []

#Cria os objetos para multiprocessamento com a utilização de um loop
#O método .start começa a execução do código
for _ in range(10):
    # Os argumentos são passados à função na criação do objeto com o parâmetro args do método Process
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    #Atribui os processos à lista processes
    processes.append(p)

#Loop que sincroniza a finalização de todos os processos filho
for process in processes:
    process.join()


#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')