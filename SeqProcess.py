import os;
from spider2 import Spider
from general import *

#Classe que lidará com cada sequencia individualmente
class SeqProcess:

    project_name = ''
    seq_name = ''
    seq_link = ''

    #Se for double strand irá ter modo diferente na main
    #Receberá link da sequência para pegar o nome, criará pasta para si
    def __init__(self, link, projectname):
        seq_link = link
        seq_name = Spider.find_name(link)
        project_name = projectname
        create_process_dir(project_name, seq_name)


    #escrever em arq processados
    #pegar nome thread is nicee

    #Analisa o tipo da sequência, se é double strand, pega nome
    def analisa_link(self):

    def baixaSequencia(self):
        os.system('/data/osvaldo/projeto_barbara/softwares/sratoolkit.2.8.0-centos_linux64/bin/fastq-dump{}'.format(self.seq_name))

    def renomear_sequencias(self):
        os.system()

    def program_star(self):
        os.system('nohup ./STAR-master/STAR-master/bin/Linux_x86_64/STAR --runMode alignReads --runThreadN 3 --genomeDir /data/barbara.perim/indiceGenoma --readFilesIn /data/osvaldo/projeto_barbara/libs/rename_ERR1971066_1.fastq.gz /data/osvaldo/projeto_barbara/libs/rename_ERR1971066_2.fastq.gz --outReadsUnmapped Fastx --readFilesCommand zcat &')

    def program_trinity(self):
        os.system('Trinity --seqType fq --max_memory 20G --left Unmapped.out.mate1  --right Unmapped.out.mate2 --output /data/barbara.perim/{}trinity_output --CPU 4 --min_contig_length 1000 --jaccard_clip --trimmomatic --full_cleanup'.format(self.project_name+'/'+self.seq_name+'/'))

    def program_blastX(self):
        os.system('/data/barbara.perim/BLAST/ncbi-blast-2.6.0+/bin/blastx -query trinity_output.Trinity.fasta -db BlastDB/viral_protein1/viral.1.protein.faa  -out blast_output -evalue 1e-5 -outfmt 0 -num_threads 4'')

    def analisaResultado(self):

    def apagaArquivos(self):

    #Realizará o processo completo, chamando os métodos
    def processo(url):


