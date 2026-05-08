import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Área do Círculo\n")

pi = 3.14
raio = float(input("Digite o raio do círculo: "))

resultado = pi * raio**2

print(f"\nA área do círculo é: {resultado:.2f}")