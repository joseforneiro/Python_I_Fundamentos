import os
import pandas as pd
os.system('cls' if os.name=='nt' else 'clear')
from funcoes import* # Isso faz com que possamos somente usar o nome da função que está em funções

try:
    titulos = extrair_titulos("https://www.globo.com/","h2.post__title")

    # criando o DataFrame
    df = pd.DataFrame(titulos)

    # salvando em CSV
    df.to_csv("titulos.csv", index=False)

    # sakvabdi en JSON
    df.to_json("titulos.json", orient="records", indent=4, force_ascii=False)

    print("\nArquivos CSV e JSON criados com sucesso!!!")

except Exception as erro:
        
    print(f"Erro: {erro}")