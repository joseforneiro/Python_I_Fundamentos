import requests
from bs4 import BeautifulSoup

url = "https://eventos.sp.senac.br/"

requisicao = requests.get(url)

site = BeautifulSoup(requisicao.text, "html.parser") # Transforma o texto em html

print(site.prettify()) # organiza o texto html