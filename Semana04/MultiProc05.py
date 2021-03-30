#Programa que realiza processamento de imagens
#Multiprocessamento é particularmente eficiente em CPU bound processes
#Este é um programa que ainda depende de operações de I/O para acessar as imagens
#No entanto o processamento em si é CPU bound


#Importa a biblioteca para multiprocessamento
import multiprocessing

#Importa a biblioteca com as funções de tempo
import time

#Importa a biblioteca de Process Pool do python
import concurrent.futures

#Importa funções de manipulação de imagens
#Utiliza a biblioteca pillow, já que a PIL é incompatível com python 3.6
from PIL import Image, ImageFilter


#Lista com o nome das imagens a serem modificadas
img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

#Registra o tempo de início de execução do programa
t1 = time.perf_counter()

#Cria um vetor com os parâmetros de resolução em pixels da imagem processada
size = (1200, 1200)

#Função de processamento de imagem
def process_image(img_name):
    #Abre o arquivo da imagem
    img = Image.open(img_name)

    #Aplica o filtro na imagem
    img = img.filter(ImageFilter.GaussianBlur(15))

    #Ajusta a resolução da imagem
    img.thumbnail(size)
    #Salva a imagem processada
    img.save(f'processed/{img_name}')
    #Exibe o resultado da operação
    print(f'{img_name} was processed...')

#Utiliza o gerenciador de contexto para acessar as funções do ProcessPoolExecutor
#Para executar utilizando threads basta modificar o método para .ThreadPoolExecutor
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Cria um processo para executar o processamento de cada imagem na lista com o método .map
    executor.map(process_image, img_names)

#Registra o tempo de término da execução
t2 = time.perf_counter()

#Exibe o tempo em que o programa ficou em execução, em secundos
#A partir da diferença entre o começo e fim da execução
print(f'Finished in {t2-t1} seconds')