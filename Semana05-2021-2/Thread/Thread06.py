#Utiliza theads para executar o código de forma mais eficiente
#Além disso agora iremos criar as threads de forma manual
#Variação de Thread05 que usa um loop dentro de uma lista para criar as threads

#Importa a biblioteca com as funções de tempo
import time

#Importa biblioteca com as funções para programação com threads (nessa versão não é utilizada)
import threading

#Importa a biblioteca de Threading Pool do python
import concurrent.futures

#Registra o tempo de início de execução do programa
start = time.perf_counter()


#Função que gera dois outputs intercalados por uma espera do programa
#Serve para simulação de I/O e fornece visualização do que está sendo executado ao usuário
#Agora aceita como argumento quantos segundos deve esperar
#A função retorna uma string que informa por quanto tempo a função esperou
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    #time.sleep(x) é o método que faz o programa dormir por x segundos
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

#Utiliza o gerenciador de contexto para acessar as funções do ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    #Lista com os tempos de espera das threads
    secs = [5, 4, 3, 2, 1]
    #Cria a lista com o loop, passando como argumento os itens da lista secs
    results = [executor.submit(do_something, sec) for sec in secs]

    #Loop que usa o método as_completed para exibir o retorno das threads
    for f in concurrent.futures.as_completed(results):
        print(f.result())



#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')

#É possível perceber que com a utilização de threads é possível realizar a função do_something duas vezes
#em um segundo.