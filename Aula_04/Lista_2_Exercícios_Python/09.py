import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Contagem Regressiva:\n")

numero = int(input("Digite um número: "))

for i in range(numero,-1,-1):
    print(i)