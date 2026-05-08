import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Dobro, triplo e quadrado")

numero = float(input("\nDigite o número: "))

dobro = 2 * numero
triplo = 3 * numero
quadrado = numero**2

print(f"\nDobro: {dobro:.2f} \nTriplo: {triplo:.2f} \nQuadrado: {quadrado:.2f}")