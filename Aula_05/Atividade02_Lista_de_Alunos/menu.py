import os
import funcoes as fn

alunos = []

while True:
    os.system('cls' if os.name=="nt" else "clear")

    print("*** Mini Calculadora ***")
    print('''
        1 - Adicionar aluno
        2 - Listar alunos
        3 - Buscar aluno
        4 - Remover aluno
        5 - Sair    
    ''')
    opcao = int(input("Digite a opção: "))
    nome = ''

    if opcao >= 0 and opcao <= 5:
        if opcao == 1:
            nome = input("\nDigite o nome do aluno: ")
            fn.adicionar_aluno(nome, alunos)
        elif opcao == 2:
            fn.listar_alunos(alunos)
        elif opcao == 3:
            fn.buscar_aluno(nome, alunos)
        elif opcao == 4:
            fn.remover_aluno(nome, alunos)
        elif opcao == 5:
            print("\nObrigado por usar esse programa.")
            break
    else:
        print("\nOpão inválida")
    
    input("\nTecle algo para continuar")

    
