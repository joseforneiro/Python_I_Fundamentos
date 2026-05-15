import os
import random
os.system('cls' if os.name=='nt' else 'clear') 

pecas = ("pedra","papel","tesoura")

computador = random.randint(0,2) # quer que o computador gere um numero inteiro de index 0 a 2

jogador = int(input('''Escolha uma opção:
[0] - Pedra                
[1] - Papel
[2] - Tesoura                
\n'''))

print(f"\nO Computador escolheu: {pecas[computador]}")
print(f"O Jogador escolheu: {pecas[jogador]}")

# Ver a tabela no slide 49 da aula 5 para entender:
tabela = ((0,1,-1),(-1,0,-1),(1,-1,0))

jogada = tabela[computador][jogador]

if jogada == 0:
    print("\nEmpate")
elif jogada == 1:
    print("\nVence o Jogador")
elif jogada == -1:
    print("\nVence o Computador")