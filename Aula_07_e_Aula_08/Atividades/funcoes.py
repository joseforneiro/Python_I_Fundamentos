import requests
from bs4 import BeautifulSoup

def cadastro_aluno(lista, dado):
    lista.append(dado)

def cadastro_item(lista):
    nome = input("\nDigite o nome do item: ").upper()

    if nome in lista:
        print("\nJá existe esse produto na lista.")
    else:
        lista.append(nome)

def remover_item(lista):
    nome = input("\nDigite o nome do item: ").upper()

    if nome in lista:
        lista.remove(nome)
        print(f"\nO nome {nome} foi removido.")
    else:
        print("\nItem não encontrado.")

def listar_itens(lista):
    for l in lista:
        print(l)

def cadastra_numero(lista):
    numero = int(input("\nDigite o número: "))
    lista.append(numero)

def listar_numeros(lista):
    for n in lista:
        print(n)

def maior_numero(lista):
    maior = 0
    anterior = 0
    for indice, valor in enumerate(lista):
        if indice == 0:
            maior = valor
            anterior = valor
        else:
            if valor > anterior:
                maior = valor
                anterior = valor
    
    print(f"\nO maior valor é {maior}")

def menor_numero(lista):
    menor = 0
    anterior = 0
    for indice, valor in enumerate(lista):
        if indice == 0:
            menor = valor
            anterior = valor
        else:
            if valor < anterior:
                menor = valor
                anterior = valor
    
    print(f"\nO menor valor é {menor}")

def media_numero(lista):

    soma = 0
    for n in lista:
        soma += n

    print(f"A média é {soma/len(lista)}")

def extrair_titulos(url):
    requisicao = requests.get(url)

    site = BeautifulSoup(requisicao.text, "html.parser")

    titulos = site.select(".title__element.headlineMain__title")

    for t in titulos:
        print(t.text.strip())

def contar_links(url):
    requisicao = requests.get(url)
    site = BeautifulSoup(requisicao.text, "html.parser")

    links = site.find_all("a")

    for l in links:
        print(l.get("href"))

    print(f"\nQuantidade: {len(links)} links")

def titulos(url):
    requisicao = requests.get(url)
    site = BeautifulSoup(requisicao.text, "html.parser")

    titulos = site.select(".Name_OrqProductCard_Name__KsaTM")

    for t in titulos:
        print(t.text.strip())

def links(url):
    requisicao = requests.get(url)
    site = BeautifulSoup(requisicao.text, "html.parser")

    links = site.select("a")

    for l in links:
        print(l.get("href"))

def precos(url):
    requisicao = requests.get(url)
    site = BeautifulSoup(requisicao.text, "html.parser")

    preco = site.select(".Price_OrqProductCard_Price__TNBZB")

    for l in preco:
        print(l.text)