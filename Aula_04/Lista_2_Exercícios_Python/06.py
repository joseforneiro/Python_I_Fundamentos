import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Soma até parar:")

soma = 0
quantidade = 0

while True:
    numero = float(input("Digite o número a ser somado: "))

    if numero == 0:
        break

    soma += numero
    quantidade += 1

print (f"\nTotal = {soma}")
print (f"Quantidade de números digitados: {quantidade}")