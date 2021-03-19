#Programa para extração e tratamento de dados em um arquivo .txt
#Código antigo está espalhado

import os
import math

#Recebe um vetor com os dados, ordena, descobre o índice dos quartis
#Retorna o valor dos quartis
def quartil (dados):
    sort = sorted(dados)
    k = len(dados) + 1
    q1 = round(0.25*k)
    quar1 = float(sort[q1])
    if k % 2:
        q2 = round((k+1)/2)
        quar2 = float(sort[q2])
    else:
        quar2 = (float(sort[(k-1)/2])) +(float(sort[k/2]))
        quar2 = quar2/2
    q3 = round(0.75*k)
    quar3 = sort[q3]
    return quar1, quar2, quar3

#lê os dados e cria os arquivos que serão escritos
with open('Dados (1).txt') as data:
    with open('Dados tratados.txt', 'w') as new_dados:
        with open('Dados rejeitados.txt', 'w') as rej:
            #inicializa algumas variáveis, cria uma lista com os valores
            vector_data = data.read()
            vector_split = vector_data.split()
            vector = []
            n = 0
            str = ''
            #Tratamento de dados e criação da lista ordenada
            while n < len(vector_split):
                str = vector_split[n]
                str = str.rstrip('e+01')
                str = float(str)
                vector.append(str)
                n+=1
            sort_vector = sorted(vector)
            #print(len(sort_vector))

            #gera os quartis e amplitude
                    # quartis = quartil (sort_vector)
                    # amplitude = sort_vector[quartis[2]] - sort_vector[quartis[0]]
                    # menor = sort_vector[quartis[0]] - 1.5 * amplitude
                    # maior = sort_vector[quartis[2]] + 1.5 * amplitude

            quartis = quartil(vector)
            amplitude = quartis[2] - quartis[0]
            menor = quartis[0] - 1.5 * amplitude
            maior = quartis[2] + 1.5 * amplitude

            #verificação dos valores para fim de debug
            print(quartis)
            print(amplitude)
            print(menor, '  ---   ', maior)

            #Escrita do arquivo com os dados aceitos e rejeitados
            n = 0
            z = 0
            while n < len(vector_split):
                if vector[n] < menor or vector[n] > maior:
                    rej.write('{}:  {}+e01 \n'.format(n, vector[n]))
                    z+= 1
                else:
                    new_dados.write('{}:  {}+e01 \n'.format(n + 1, vector[n]))
                n += 1