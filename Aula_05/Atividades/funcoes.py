def calculadora(a,b,op):
    if op == 1:
        return a + b
    elif op == 2:
        return a - b
    elif op == 3:
        return a * b
    elif op == 4:
        return a / b if b != 0 else "Erro: Divisão por zero."
    else: return "Opção inválida"

# Outro modo de fazer:
def calculadora2(a,b,op):
    operacoes = {
        1:a+b,
        2:a-b,
        3:a*b,
        4:a/b if b!=0 else "Erro: Divisao por zero"
    }
    return operacoes[op]

def adicionar_aluno(nome, lista):
    if nome in lista:
        print("\nO nome já existe na lista.")
    else:
        lista.append(nome)

def listar_alunos(lista):
    if len(lista) > 0:
        for nome in lista:
            print(f"Nome: {nome}.")
    else:
        print("\nA lista está vazia!!!")

def buscar_aluno(nome, lista):
    if nome in lista:
        print(f"Existe o nome {nome} na lista.")
    else:
        print("Não existe o nome {nome} na lista!!!")

def remover_aluno(nome, lista):
    if nome in lista:
        lista.remove(nome)
        print("\nnome removido com sucesso.")
    else:
        print("\nNome não encontrado na lista!!!")

