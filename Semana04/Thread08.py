#Programa que baixa imagens de alta resolução com a utilização de threads
#Devido a natureza I/O bound de downloads, a utilização de threads fornece uma grande melhora de desempenho


#Importa biblioteca requests, responsável por acessar o servidor que iremos acessar
import requests
#Importa biblioteca com as funções de tempo
import time
#Importa bibliotece que responsável pelas funções de threads
import concurrent.futures


#Lista com o endereço das imagens a serem baixadas
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

#Registra o tempo de início de execução do programa
t1 = time.perf_counter()

#Função que realiza o download das imagens
#Possui como argumento o url da imagem
def download_image(img_url):
    #Realiza o download dos dados contidos na imagem em forma de bytes
    img_bytes = requests.get(img_url).content
    #Faz o parsing da url para o nome do arquivo .jpg
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    #Cria o arquivo com o nome desejado, em modo de gravação em bytes
    with open(img_name, 'wb') as img_file:
        #Grava os dados do arquivo
        img_file.write(img_bytes)
        #Exibe o resultado
        print(f'{img_name} was downloaded...')

#As próximas linhas de código servem para executar o programa de forma síncrona
# for img_url in  img_urls:
#     download_image(img_url)

#Utiliza o gerenciador de contextos para o ThreadPoolExecutor
#Este bloco é responsável pela execução assíncrona do programa
with concurrent.futures.ThreadPoolExecutor() as executor:
    #Cria uma thread para executar download_image para cada url na lista a ser baixada com o método .map
    executor.map(download_image, img_urls)

#Registra o tempo de término da execução
t2 = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em segundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {t2-t1} seconds')