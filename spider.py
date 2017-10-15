from general import *
from bs4 import BeautifulSoup
import requests

class Spider:

    # Variaveis compartilhadas entre todas as instancias
    project_name = ''
    base_url = '' #Será util:?????
    domain_name = ''
    queue_file = ''
    current_page_file = ''
    next_page_file = ''
    current_page = ''
    next_page = ''

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.current_page = base_url
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.current_page_file = Spider.project_name + '/currentpage.txt'
        Spider.next_page_file = Spider.next_page_file + 'nextpage.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():  # Cria projeto e arquivos
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)

    #Analisa página e pega links, JÁ COLOCO NO ARQ? é o proximapagina
    #crawl o pagina atual e no fim ele chama o get next page
    #atualizando o pagina atual e proxima
    #def crawl_page(self):

    #Encontra os links da página atual e os coloca no arquivo fila
    @staticmethod
    def find_links():
        links = []
        page = requests.get(Spider.current_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        for result in soup.select('div.rslt a'): #pega resultados
            links.append(result['href'])
        for result in links:
            append_to_file(Spider.queue_file, result)
    #Deve adicionar a próxima página para página atual e atualizar próxima página



    #Dado o link da sequência é retornado o nome dela para download
    @staticmethod
    def find_name(url):
         page = requests.get(url)
         soup = BeautifulSoup(page.content, 'html.parser')
         name = soup.select('div#ResultView table a')
         return name[0].get_text()

    # Pega o link para proxima pág
    #def get_next_page():

Spider('VirHuSeq2','https://www.ncbi.nlm.nih.gov/sra/?term=human+AND+RNA','www.ncbi.nlm.nih.gov/')
Spider.find_links()