import os
import requests
from bs4 import BeautifulSoup
os.system('cls' if os.name=='nt' else 'clear')

url = "https://www.cnnbrasil.com.br/"

requisicao = requests.get(url)

site = BeautifulSoup(requisicao.text, "html.parser") # Transforma o texto em html

titulos = site.select("h2 a")

for t in titulos:
    # print(t.text)
    print(t.get("href")) # O .get() pega um atributo, no exemplo ele está pegando o atributo href da tag a


