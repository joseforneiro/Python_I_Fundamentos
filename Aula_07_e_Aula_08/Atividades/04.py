import os
import funcoes as fn
os.system('cls' if os.name=='nt' else 'clear')

try:
    url = "https://www.uol.com.br"

    fn.extrair_titulos(url)

except Exception as erro:
    print(f"Erro: {erro}")