import os
import requests
os.system('cls' if os.name=='nt' else 'clear')

cep = input("Digite um CEP: ")

url = f"http://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(url, verify=False)

dados = requisicao.json()

# print(dados)
# print(dados["logradouro"])

for chave, valor in dados.items():
    print(chave, ":", valor)