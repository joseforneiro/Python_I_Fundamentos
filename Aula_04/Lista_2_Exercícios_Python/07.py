import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Média de 5 notas:\n")

soma = 0
media = 0
maior = 0
menor = 0

for i in range(1,6):
    numero = int(input(f"Digite a nota {i}: "))
    soma += numero
    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero >= maior:
            maior = numero
        else:
            menor = numero
    
media = soma / 5

print(f"\nMédia: {media}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
