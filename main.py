import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
from SeqProcess import SeqProcess

PROJECT_NAME = 'VirHuSeq'
HOMEPAGE = 'https://www.ncbi.nlm.nih.gov/sra/?term=human+AND+RNA'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
PROCESSED_FILE = PROJECT_NAME + '/processed.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 3
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

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
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Lê o arquivo fila, se estiver vazio vai para proxima pagina, se não houver proxima para
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0: #saber se ainda há algo pra ser crawled
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()
    else: #Quando não houver nada na fila, ele irá para a próxima página
        if Spider.next_page(): #Se não houver próxima página ele para
            crawl()