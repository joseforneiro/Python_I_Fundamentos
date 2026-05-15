import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

# *****************************************************
# *** notebookLM -> IA para melhorar a documentação ***
# *****************************************************

# Criação da função:
def saudacao():
    print("Olá!")

saudacao() # Chamando a função (executando)

# Criação de função com parâmetro
def saudacao1(nome):
    print(f"Olá, {nome}")

saudacao1("Junior")

# Criação de função com parâmetros e retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(5, 8)

print(resultado)