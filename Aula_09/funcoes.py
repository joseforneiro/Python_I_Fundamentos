import requests
from bs4 import BeautifulSoup

def acessar_site(url):
    try:
        if url:
            requisicao = requests.get(url)
            return BeautifulSoup(requisicao.text, "html.parser")
        else:
            print("\nInformar um site válido!!!")
    
    except Exception as erro:
        print(f"Erro: {erro}")   

def extrair_titulos(url,seletor):
    try:
        site = acessar_site(url)
        titulos_html = site.select(seletor)
        titulos = []

        for t in titulos_html:
            if t:
                titulos.append(t.text.strip()) # O strip tira os espaços
        
        for titulo in titulos:
            print(titulo)
        
        return titulos
    
    except Exception as erro:
        print(f"Erro: {erro}")   