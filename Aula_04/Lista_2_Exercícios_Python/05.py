import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Soma dos dígitos:\n")

numero = input("Digite um número inteiro: ")
lista = list(numero)

soma = 0

for i in range(0, len(lista)):
    soma += int(lista[i])

print(f"\nSoma dos dígitos: {soma}")
