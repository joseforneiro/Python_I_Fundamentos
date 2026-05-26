import requests
from bs4 import BeautifulSoup
import os
os.system('cls' if os.name=='nt' else 'clear')

url = "https://eventos.sp.senac.br/"

requisicao = requests.get(url)

site = BeautifulSoup(requisicao.text, "html.parser") # Transforma o texto em html

titulos = site.find_all("ul", class_="event_date")
dataT = site.find_all("time")

# for t in titulos:
#     print(t.text)

for data in dataT:
    print(data.text)

