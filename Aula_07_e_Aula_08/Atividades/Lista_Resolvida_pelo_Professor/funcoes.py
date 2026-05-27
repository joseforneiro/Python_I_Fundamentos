import requests
from bs4 import BeautifulSoup

def cadastrar_aluno(nome, nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4) / 4
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    aluno = (nome, media, situacao)
    return aluno

def adicionar_item(lista, item):
    try:
        if item not in lista:
            lista.append(item)
            lista.sort() # ordena a lista em ordem alfabética
        else:
            print("\nEsse item já existe na lista")

    except Exception as erro:
        print(f"Erro: {erro}")

def remover_item(lista, item):
    try:
        if item in lista:
            lista.remove(item)
        else:
            print("\nItem não encontrado na lista")

    except Exception as erro:
        print(f"Erro: {erro}")

def listar_itens(lista):
    try:
        if len(lista) > 0:
            for i in lista:
                print(i)
        else:
            print("\nA lista está vazia")

    except Exception as erro:
        print(f"Erro: {erro}")

def maior_numero(lista):
    try:
        # maior = lista[0]
        # for n in lista:
        #     if n > maior:
        #         maior = n
        # return maior

        # ou

        return max(lista) # Função python para retornar o maior valor
    except Exception as erro:
        print(f"Erro: {erro}")

def menor_numero(lista):
    try:
        return min(lista) # Função python para retornar o menor valor
    
    except Exception as erro:
        print(f"Erro: {erro}")

def media_numero(lista):
    try:
        return sum(lista) / len(lista) # sum -> função python para somar itens de uma lista. len -> Conta quantos itens tem em uma lista.
    
    except Exception as erro:
        print(f"Erro: {erro}")

def numeros_pares(lista):
    try:
        pares = []
        for n in lista:
            if n % 2 == 0:
                pares.append(n)

        return pares
    
    except Exception as erro:
        print(f"Erro: {erro}")

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


    except Exception as erro:
        print(f"Erro: {erro}")

def extrair_links(url,seletor):
    try:
        site = acessar_site(url)
        links_html = site.select(seletor)
        links = []

        for l in links_html:
            if l:
                links.append(l.get("href"))
        
        for lin in links:
            print(lin)

        return f"{len(links)} links"

    except Exception as erro:
        print(f"Erro: {erro}")