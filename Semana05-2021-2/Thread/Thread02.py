#Primeira versão apresentada no vídeo
#Programa que apenas dorme, com o propósito de simular uma espera por I/O
#Utiliza theads para executar o código de forma mais eficiente


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

#Cria duas threads como os objetos t1 e t2
#Nesse momento nenhum código é executado
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)


#Inicia a execução das threads
t1.start()
t2.start()

#O método join faz com o programa principal espere pela finalização das threads
#O que serve para realizar sincronização entre as threads
#Sem o join por exemplo, este programa exibiria que foi finalizado em 0 segundos
# enquanto as duas threads ainda estariam dormindo
t1.join()
t2.join()

#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')

#É possível perceber que com a utilização de threads é possível realizar a função do_something duas vezes
#em um segundo.