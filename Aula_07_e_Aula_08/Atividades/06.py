import os
import funcoes as fn

url = "https://www.buscape.com.br/"

try:
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("*** Sistema de Scraping ***")
        print('''
        [1] - Extrair títulos
        [2] - Extrair links
        [3] - Extrair preços
        [4] - Sair
        ''')
        opcao = int(input("Digite a opção: "))

        if opcao == 4:
            break

        if opcao >= 1 and opcao <= 3:
            if opcao == 1:
                fn.titulos(url)
            if opcao == 2:
                fn.links(url)
            if opcao == 3:
                fn.precos(url)
        else:
            print("\nOpção inválida!!!")
        
        input("\nTecle Enter para continuar...")
    
    

except Exception as erro:
    print(f"Erro: {erro}")