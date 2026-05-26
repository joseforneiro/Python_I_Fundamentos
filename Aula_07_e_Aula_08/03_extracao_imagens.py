# Bibliotecas Utilizadas:
import os # Importa funções do sistema operacional
import requests # Importa biblioteca para fazer requisições HTTP
from bs4 import BeautifulSoup # Importa a classe BeautifulSoup
from urllib.parse import urljoin # Importa a função para montar URL completa

os.system('cls' if os.name=='nt' else 'clear') # Limpa o terminal do Windows
url = "https://eventos.sp.senac.br/" # URL do site
os.makedirs("Aula_07/imagens", exist_ok=True) # Cria a pasta imagens caso ela não exista
requisicao = requests.get(url) # Faz requisição para acessar o site
site = BeautifulSoup(requisicao.text, "html.parser") # Interpreta o HTML da página

imagens = site.find_all("img") # Busca todas as tags <img>

for img in imagens: # Percorre todas as imagens encontradas
    caminho = img.get("src") # Obtém o valor do atributo src da imagem
    if caminho: # Verifica se o src existe
        url_imagem = urljoin(url, caminho) # Monta URL completa da imagem
        nome = url_imagem.split("/")[-1] # Obtem o nome da imagem pela URL
        nome = nome.split("?")[0] # Remove parâmetros extras da URL
        imagem = requests.get(url_imagem) # Faz o download da imagem
        with open(f"Aula_07/imagens/{nome}", "wb") as arquivo: # Cria arquivo em modo binário
            arquivo.write(imagem.content) # Salva os bytes da imagem no arquivo
        print(f"{nome} salva!") # Mostra mensagem de sucesso