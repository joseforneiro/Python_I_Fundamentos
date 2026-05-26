import os
import funcoes as fn

lista_numeros = []
try:
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("*** Análise de Números ***")
        print('''\n
        [1] - Cadastrar números
        [2] - Listar números
        [3] - Retornar maior número
        [4] - Retornar menor número
        [5] - Retornar média 
        [6] - Sair
        ''')
        opcao = int(input("Digite a opção: "))

        if opcao == 6:
            break

        if opcao >= 1 and opcao <= 5:
            if opcao == 1:
                fn.cadastra_numero(lista_numeros)
            if opcao == 2:
                fn.listar_numeros(lista_numeros)
            if opcao == 3:
                fn.maior_numero(lista_numeros)
            if opcao == 4:
                fn.menor_numero(lista_numeros)
            if opcao == 5:
                fn.media_numero(lista_numeros)
        else:
            print("\nOpção inválida!!!")
        
        input("\nTecle Enter para continuar...")
    
    

except Exception as erro:
    print(f"Erro: {erro}")