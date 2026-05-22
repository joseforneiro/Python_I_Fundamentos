import os
import funcoes as fn


try:
    lista_itens = []    
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("*** Lista de Compras Inteligente ***")
        print('''\n
        [1] - Cadastrar item
        [2] - Remover item
        [3] - Listar itens
        [4] - Sair
        ''')
        opcao = int(input("\nDigite a opção: "))

        if opcao == 4:
            break

        if opcao >= 1 and opcao <= 3:
            if opcao == 1:
                fn.cadastro_item(lista_itens)
            elif opcao == 2:
                fn.remover_item(lista_itens)
            elif opcao == 3:
                fn.listar_itens(lista_itens)
        else:
            print("\nOpção inválida!!!")
        
        input("\nTecle Enter para continuar...")



except Exception as erro:
    print(f"Erro: {erro}")