import os
os.system('cls')

numero = int(input("Digite um número inteiro: "))
pares = 0
impares = 0

while numero > 0:
    digito = numero % 10

    if digito % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    numero //=10 # é a mesma coisa que numero = numero // 10

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")
