import os
import funcoes as fn

alunos = []

while True:
    os.system('cls' if os.name=="nt" else "clear")

    print("*** Lista de Alunos ***")
    print('''
        [1] - Adicionar aluno
        [2] - Listar alunos
        [3] - Buscar aluno
        [4] - Remover aluno
        [5] - Sair    
    ''')
    opcao = int(input("Digite a opção: "))
    nome = ''

    if opcao > 0 and opcao < 6:
        if opcao == 1:
            nome = input("\nDigite o nome do aluno: ").upper()
            fn.adicionar_aluno(nome, alunos)
        elif opcao == 2:
            fn.listar_alunos(alunos)
        elif opcao == 3:
            nome = input("\nDigite o nome do aluno: ").upper()
            fn.buscar_aluno(nome, alunos)
        elif opcao == 4:
            nome = input("\nDigite o nome do aluno: ").upper()
            fn.remover_aluno(nome, alunos)
        elif opcao == 5:
            print("\nObrigado por usar esse programa.")
            break
    else:
        print("\nOpção inválida")
    
    input("\nPrecione <ENTER> para continuar...")

    
