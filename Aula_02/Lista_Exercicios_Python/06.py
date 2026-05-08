import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Número positivo, negativo ou zero\n")

numero = float(input("Informe o número: "))

if numero > 0: 
    resultado = "O número é positivo"
elif numero < 0:
    resultado = "O número é negativo"
else:
    resultado = "O número é zero"

print(f"\n{resultado}")
