import requests
import bs4
import os
import time
from CConexao import Conexao


class DownloaderPornHub:

    def __init__(self, _pasta_saida, _pesquisa, _pagina_inicial, _pagina_final):
        self.pasta_saida = _pasta_saida
        self.pesquisa = _pesquisa
        self.pg_inicial = _pagina_inicial
        self.pg_final = _pagina_final
        self.i = 1
        self.tent = 0
        self.conexao = Conexao()

    def download(self):
        if self.conexao.get_status():
            for self.i in range(self.pg_inicial, self.pg_final):
                response = requests.get(str('https://pt.pornhub.com/video/search?search=' + self.pesquisa + '&page=' + str(self.i)))
                soup = bs4.BeautifulSoup(response.text, "html.parser")
                for div in soup.find_all(class_='img fade fadeUp videoPreviewBg'):  # img fade videoPreviewBg fadeUp é a classe de div que contem os links
                    link = "https://pt.pornhub.com" + str(div.find('a')['href'])
                    comando = 'youtube-dl \"' + link + '\"' + ' --output \\' + self.pasta_saida + '\\%(title)s.%(ext)s'
                    os.system(comando)
        else:
            self.tent += 1
            print("Sem conexão... Tentativa " + str(self.tent))
            time.sleep(5)