from urllib.parse import urlparse

#Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.') #lists of 3, split no ponto
        return results [-5] + '.' + results [-4] + '.' + results[-3] + '.' + results[-2] + '.' + results[-1] #adiciona o ponto no meio
    except:
        return 'Error'

#Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc #Pega a parte do link entre o protocolo e o fim
    except:                         #ex.: youtube.com
        return 'Error'


