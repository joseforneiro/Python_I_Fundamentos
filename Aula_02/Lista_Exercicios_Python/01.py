import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Média Aritmética:\n")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segunto número: "))

media = (numero1 + numero2) / 2

print(f"\nA média aritmética é {media:.2f}")
