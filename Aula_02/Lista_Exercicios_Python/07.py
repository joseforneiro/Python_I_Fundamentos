import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Maior entre dois números\n")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    resultado = numero1
elif numero1 < numero2:
    resultado = numero2
else:
    resultado = "Os números são iguais"

print(f"\nResultado: {resultado}")

