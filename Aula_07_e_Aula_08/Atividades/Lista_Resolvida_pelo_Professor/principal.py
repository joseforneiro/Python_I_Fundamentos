import os
from funcoes import* # Isso faz com que possamos somente usar o nome da função que está em funções
os.system('cls' if os.name=='nt' else 'clear')

def exe01():
    try:
        lista_alunos = []
        quanti_alunos = int(input("\nQuantos alunos quer cadastrar? "))

        for i in range(quanti_alunos):
            nome = input("\nDigite o nome do aluno: ")
            n1 = float(input("Digite a 1ª Nota: "))
            n2 = float(input("Digite a 2ª Nota: "))
            n3 = float(input("Digite a 3ª Nota: "))
            n4 = float(input("Digite a 4ª Nota: "))

            aluno = cadastrar_aluno(nome,n1,n2,n3,n4)
            if aluno:
                lista_alunos.append(aluno)
        
        for al in lista_alunos:
            print(f"Nome = {al[0]} - Média = {al[1]:.2f} - Situação = {al[2]}")

    except Exception as erro:
        print(f"Erro: {erro}")

def exe02():
    try:
        lista = []
    
        while True:
            print('''\n
            [1] - Add produto
            [2] - Remover produto
            [3] - Listar produtos
            [4] - Sair
            ''')
            opcao = input("\nDigite a opção: ")

            if opcao == "1":
                produto = input("\nDigite o produto: ").upper()
                adicionar_item(lista, produto)
            elif opcao == "2":
                produto = input("\nDigite o produto: ").upper()
                remover_item(lista, produto)
            elif opcao == "3":
                listar_itens(lista)
            elif opcao == "4":
                break
            else:
                print("\nDigite uma opção válida")
        
        print("Exercício 2 finalizado")

    except Exception as erro:
        print(f"Erro: {erro}")

def exe03():
    try:
        lista = [1,2,3,4,5,6,7,8,9,10]

        print(f"Maior número: {maior_numero(lista)}")
        print(f"Menor número: {menor_numero(lista)}")
        print(f"Média: {media_numero(lista)}")
        print(f"Números pares: {numeros_pares(lista)}")


    except Exception as erro:
        print(f"Erro: {erro}")    

def exe04():
    try:
        extrair_titulos("https://www.globo.com/","h2.post__title")

    except Exception as erro:
        print(f"Erro: {erro}")

def exe05():
    try:
        quantidade = extrair_links("https://www.uol.com/","a")
        print(quantidade)
        
    except Exception as erro:
        print(f"Erro: {erro}")


exe05()