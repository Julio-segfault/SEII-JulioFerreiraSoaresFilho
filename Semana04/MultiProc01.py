#Versão de Thread01.py que utiliza processamento em paralelo


#Importa a biblioteca para multiprocessamento
import multiprocessing

#Importa a biblioteca com as funções de tempo
import time

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa de 1 segundo
#Simula uma operação de I/O ou execução de código
def do_something():
    print(f'Sleeping 1 second...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(1)
    print(f'Done Sleeping...')

#Cria os objetos para multiprocessamento
#Nesse estágio não ocorre execução do código
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)


#Inicia a execução dos códigos com paralelismo
p1.start()
p2.start()

#O método .join sincroniza os processos criados com a execução do programa principal
#Sem o join o programa principal seria finalizado antes dos processos filhos, e exibiria uma execução de 0 segundos
p1.join()
p2.join()

#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')