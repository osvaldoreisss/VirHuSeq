import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Criando projeto: {}'.format(directory))
        os.makedirs(directory)

def create_process_dir(project_name, process):
    if not os.path.exists(process):
        print ('Criando processo: {}'.format(process))
        os.makedirs(project_name + '/' + process)

#Criar arquivos crawled, se ainda não tiverem sido criados
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt' #paginas na fila para ser crawled
    processed = project_name + '/processed.txt'
    current_page = project_name + 'currentpage.txt'
    next_page = project_name + 'nextpage.txt'
    if not os.path.isfile(queue):
        write_file(queue, '')
    if not os.path.isfile(processed):
        write_file(processed, '')
    if not os.path.isfile(current_page):
        write_file(current_page, base_url)
    if not os.path.isfile(next_page):
        write_file(next_page, '')

#Cria um novo arquivo
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#Adiciona a informação em um arquivo existente
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Deleta o conteúdo de um arquivo
def delete_file_content(path):
    with open(path, 'w'):
        pass #não faz nada

#Ler um arquivo e converter cada linha para items set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f: #rt apenas para ler
        for line in f:
            results.add(line.replace('\n', '')) #tirando a new line
    return results

#Cada item de um set vira uma linha em um arquivo
def set_to_file(setlinks, file):
    delete_file_content(file)
    for link in sorted(setlinks): #coloca em ordem alfabetica
        append_to_file(file, link)

