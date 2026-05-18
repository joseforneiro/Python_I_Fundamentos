import os
os.system('cls' if os.name=="nt" else "clear")
import funcoes as fn

while True:

    print("*** Mini Calculadora ***")
    numero1 = int(input("\nDigite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    print('''
          [1] - Somar
          [2] - Subtrair
          [3] - Multiplicar
          [4] - Dividir
          [5] - Sair
    ''')

    operacao = int(input("Digite a opção: "))

    if operacao == 5:
        break

    resultado = fn.calculadora(numero1,numero2,operacao)

    print(f"\nO resultado é {resultado}")

