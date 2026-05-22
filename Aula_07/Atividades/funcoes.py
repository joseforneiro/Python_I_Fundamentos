def cadastro_aluno(lista, dado):
    lista.append(dado)

def cadastro_item(lista):
    produto = input("\nDigite o nome do item: ").upper()

    if produto in lista:
        print("\nJá existe esse produto na lista.")
    else:
        lista.append(produto)

def remover_item(lista):
    produto = input("\nDigite o nome do item: ").upper()

    if produto in lista:
        lista.remove(produto)
    else:
        print("\nItem não encontrado.")

def listar_itens(lista):
    for l in lista:
        print(l)
