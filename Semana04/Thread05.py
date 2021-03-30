#Utiliza theads para executar o código de forma mais eficiente
#Além disso agora iremos criar as threads de forma manual


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
    #Cria f1 e f2 como um objeto future. O método submit agenda a execução do código, passa os argumentos e retorna o objeto
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    #Exibe a string de retorno da thread executada
    print(f1.result())
    print(f2.result())



#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')

#É possível perceber que com a utilização de threads é possível realizar a função do_something duas vezes
#em um segundo.