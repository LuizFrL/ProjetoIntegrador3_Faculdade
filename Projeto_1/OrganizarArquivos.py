from ProjetoIntegrador3_Faculdade.Projeto_1.Diretorio import ArquivosDir
from ProjetoIntegrador3_Faculdade.Projeto_1.InformacoersArquivos import ArquivoInf
import os, shutil


class OrganizarArquivos(ArquivosDir):
    def __init__(self, diretorio_raiz, diretorio_destino):
        ArquivosDir.__init__(self, diretorio_raiz)
        self.diretorio_destino = diretorio_destino

    def __organizar_lista_arquivos(self, config=None, pasta_nao_regis=''):
        if config is None:
            config = {
                        'Imagens': ['.jpeg', '.png', '.jpg', '.gif', '.bmp'],
                        'Videos': ['.mp4', '.mkv', '.amv'],
                        'Documentos': ['.docx', '.pdf', '.xlsx', '.csv', '.xltx', '.xls', '.txt'],
                  }
        lista_arquivos = {}

        for key in config.keys():
            lista_arquivos[key] = []

        arquivos_lidos = []
        todos_arquivos = set(self.arquivos())

        for arquivo in todos_arquivos:
            arq = ArquivoInf(arquivo)
            for pasta, extensoes in config.items():
                for extensao in extensoes:
                    if extensao.lower().find(arq.extensao_arquivo()) != -1:
                        lista_arquivos[pasta].append(arquivo)
                        arquivos_lidos.append(arquivo)

        if pasta_nao_regis:
            if lista_arquivos.get(pasta_nao_regis):
                pasta_nao_regis += '(1) - Cópia'
            arquivos_nao_registrados = todos_arquivos.difference(set(arquivos_lidos))
            lista_arquivos[pasta_nao_regis] = list(arquivos_nao_registrados)
        return lista_arquivos

    def organizar_arquivos(self, config=None, pasta_nao_regis=''):
        arquivos_organizados = self.__organizar_lista_arquivos(config, pasta_nao_regis)
        for pasta, arquivos in arquivos_organizados.items():
            nova_pasta = self.diretorio_destino + r'\{}'.format(pasta)
            os.makedirs(nova_pasta)
            for arquivo in arquivos:
                novo_diretorio = nova_pasta + r'\{}'.format(os.path.basename(arquivo))
                shutil.move(arquivo, novo_diretorio)
                print(f"""Arquivo: {os.path.basename(arquivo)}
De: {arquivo}
Para: {novo_diretorio}
""")
