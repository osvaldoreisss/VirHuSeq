import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from SeqProcess import SeqProcess

NOME_PROJETO = 'VirHuSeq'
HOMEPAGE = 'https://www.ncbi.nlm.nih.gov/sra/?term=human+AND+RNA'
NOME_DOMINIO = get_domain_name(HOMEPAGE)
ARQ_FILA = NOME_PROJETO + '/queue.txt'
ARQ_PROCESSADOS = NOME_PROJETO + '/processados.txt'
CRAWLED_FILE = NOME_PROJETO + '/crawled.txt'
NUMBER_OF_THREADS = 3
queue = Queue()
Spider(NOME_PROJETO,HOMEPAGE,NOME_DOMINIO)

def criar_processos():
    for _ in range (NUMBER_OF_THREADS):
        t = threading.Thread(target=seq_processos)
        t.daemon = True  # morre quando a main fecha
        t.start()

def seq_processos():
    while True:
        url = queue.get()
        SeqProcess.processo(url)
        queue.task_done()

#Para cada link no arquivo da fila, um processo é adicionado ao queue
def create_jobs():
    for link in file_to_set(ARQ_FILA):
        queue.put(link)
    queue.join()
    crawl()

#Lê o arquivo fila, se estiver vazio vai para proxima pagina, se não houver proxima para
def crawl():
    queued_links = file_to_set(ARQ_FILA)
    if len(queued_links) > 0: #saber se ainda há algo pra ser crawled
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()
    else: #Quando não houver nada na fila, ele irá para a próxima página
        if Spider.proximapagina(): #Se não houver próxima página ele para
            crawl()