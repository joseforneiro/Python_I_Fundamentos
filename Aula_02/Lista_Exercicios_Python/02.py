import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Calculadora\n")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisao \nOpção: ")

if operacao == "1":
    resultado = numero1 + numero2
elif operacao == "2":
    resultado = numero1 - numero2
elif operacao == "3":
    resultado = numero1 * numero2
elif operacao == "4":
    resultado = numero1 / numero2
else:
    resultado = "Opção inválida"

print(f"\nO resultado da operação é: {resultado:.2f}")
