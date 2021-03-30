#Programa que cria vários processos filhos para executar uma função que simula uma operação (I/O ou execução_
#Similar a MultiProc03.py,
# mas utiliza o método .map para passar os argumentos de uma lista durante a criação dos processos filhos


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
#A parte de código comentada é similar ao Thread07.py, apenas o nome do método e das variavéis foram trocados
#A estrutura permaneceu a mesma
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Lista com os tempos de espera das threads
    secs = [5, 4, 3, 2, 1]
    # Cria a lista com o método map que executa do_something para cada valor da lista secs
    # Nesse caso results armazena os resultados da execução, na ordem em que as threads foram criadas
    results = executor.map(do_something, secs)

    # Exibe os valores de result
    for result in results:
        print(result)


#Registra o tempo de término da execução
finish = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {round(finish-start, 3)} second(s)')


#A ordem de exibição dos resultados é a mesma da criação dos processos