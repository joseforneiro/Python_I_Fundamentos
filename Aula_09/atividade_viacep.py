import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
os.system('cls' if os.name=='nt' else 'clear')

try:
    cep = input("Digite um CEP: ")

    url = f"http://viacep.com.br/ws/{cep}/json/"
    requisicao = requests.get(url, verify=False)

    dados = requisicao.json()

    print(dados)

    # for chave, valor in dados.items():
    #     print(chave, ":", valor)

    # criando o DataFrame
    df = pd.DataFrame([dados])

    # salvando em CSV
    df.to_csv("dados.csv", index=False)

    # sakvabdi en JSON
    df.to_json("dados.json", orient="index", indent=4, force_ascii=False)

    print("\nArquivos CSV e JSON criados com sucesso!!!")

except Exception as erro:
    print(f"Erro: {erro}")