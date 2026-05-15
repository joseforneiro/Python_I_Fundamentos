def adicionar_aluno(nome, lista):
    lista.append(nome)

def listar_alunos(lista):
    for nome in lista:
        print(nome)

def buscar_aluno(nome, lista):
    if nome in lista:
        for i,nome in enumerate(lista):
            print(f"\nO nome {nome} está cadastrado na posição {i}")
    else:
        print("\nO nome informado não foi encontrado na lista.")

def remover_aluno(nome, lista):
    lista.remove(nome)
    print("\nnome removido com sucesso!!!")