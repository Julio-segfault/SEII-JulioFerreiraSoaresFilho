#Programa que cria vários processos filhos para executar uma função que simula uma operação (I/O ou execução_
#È similar à Thread05.py na utilização da biblioteca concurrent.futures
#Além apresenta a criação de um loop como em Thread06.py


#Importa a biblioteca para multiprocessamento
import multiprocessing

#Importa a biblioteca com as funções de tempo
import time

#Importa a biblioteca de Process Pool do python
import concurrent.futures

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa
#Serve para simulação de uma operação e fornece visualização do que está sendo executado ao usuário
#Agora aceita como argumento quantos segundos deve esperar
#A função retorna uma string que informa por quanto tempo a função esperou
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#Utiliza o gerenciador de contexto para acessar as funções do ProcessPoolExecutor
#A parte de código comentada é similar ao Thread05.py, apenas o nome do método e das variavéis foram trocados
#A estrutura permaneceu a mesma
with concurrent.futures.ProcessPoolExecutor() as executor:

    #Versão similar ao Thread05.py
    # #Cria f1 e f2 como um objeto future. O método submit agenda a execução do código, passa os argumentos e retorna o objeto
    # p1 = executor.submit(do_something, 1)
    # p2 = executor.submit(do_something, 1)
    # #Exibe a string de retorno da thread executada
    # print(p1.result())
    # print(p2.result())

    # Lista com os tempos de espera das threads
    secs = [5, 4, 3, 2, 1]

    #Versão que implementa um loop dentro de uma lista
    results = [executor.submit(do_something,sec) for sec in secs]

    #Loop que usa o método as_completed para exibir o retorno das threads
    for f in concurrent.futures.as_completed(results):
        print(f.result())


#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')


#A ordem em que aparecem os resultados depende do agendamento dos processos feito pelo ProcessPool
#Além do número de núcleos do processador