import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Contador de dígitos pares e impares:\n")

par = 0
impar = 0

numero = input("Digite um número inteiro: ")
lista = list(numero)


for i in range(0, len(lista)):
    if int(lista[i]) % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"\nPares: {par}")
print(f"Impar: {impar}")
