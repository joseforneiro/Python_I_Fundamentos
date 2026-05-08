import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("é par")
else:
    print("é impar")

