import os
os.system('cls')

soma = 0
cont = 0

while True:
    numero = int(input("Digite um número: "))   

    soma += numero
    cont += 1

    if numero == 0:
        cont -= 1
        break

print(f"Soma total = {soma}")
print(f"Quantidade de números digitados = {cont}")