import os
import funcoes as fn
os.system('cls' if os.name=='nt' else 'clear')

try:
    print("*** Cadastro de Alunos ***")

    quantidade = int(input("\nQuantos alunos deseja cadastrar: "))
    alunos = []

    for q in range(quantidade):
        aluno = input("\nDigite o nome do aluno: ")
        nota1 = float(input("Digite a Nota 1: "))
        nota2 = float(input("Digite a Nota 2: "))
        nota3 = float(input("Digite a Nota 3: "))
        nota4 = float(input("Digite a Nota 4: "))
        media_aluno = (nota1 + nota2 + nota3 + nota4) / 4

        temp = {
            'nome': aluno,
            'media': media_aluno,
            'situacao': "Aprovado" if media_aluno >= 7 else "Reprovado"
        }

        fn.cadastro_aluno(alunos, temp)
        
    print()
    for i in alunos:
        print(f"{i['nome']} - Média: {i['media']} - {i['situacao']}")

except Exception as erro:
    print(f"Erro: {erro}")
