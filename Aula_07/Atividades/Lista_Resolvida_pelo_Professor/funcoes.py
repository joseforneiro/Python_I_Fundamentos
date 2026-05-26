

def cadastrar_aluno(nome, nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4) / 4
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    aluno = (nome, media, situacao)
    return aluno

def adicionar_item(lista, item):
    try:
        if item not in lista:
            lista.append(item)
            lista.sort() # ordena a lista em ordem alfabética
        else:
            print("\nEsse item já existe na lista")

    except Exception as erro:
        print(f"Erro: {erro}")

def remover_item(lista, item):
    try:
        if item in lista:
            lista.remove(item)
        else:
            print("\nItem não encontrado na lista")

    except Exception as erro:
        print(f"Erro: {erro}")

def listar_itens(lista):
    try:
        if len(lista) > 0:
            for i in lista:
                print(i)
        else:
            print("\nA lista está vazia")

    except Exception as erro:
        print(f"Erro: {erro}")