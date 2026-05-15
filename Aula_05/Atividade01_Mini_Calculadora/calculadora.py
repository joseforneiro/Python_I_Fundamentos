import os
import funcoes as fn

while True:
    os.system('cls' if os.name=="nt" else "clear")

    print("*** Mini Calculadora ***")
    print('''
        1 - Somar
        2 - Subtrair
        3 - Multiplicar
        4 - Dividir     
    ''')
    operacao = int(input("Digite a opção: "))
    resultado = 0

    if operacao >= 0 and operacao <= 4:
        numero1 = float(input("\nDigite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if operacao == 1:
            resultado = fn.somar(numero1,numero2)
        elif operacao == 2:
            resultado = fn.subtrair(numero1,numero2)
        elif operacao == 3:
            resultado = fn.multiplicar(numero1,numero2)
        elif operacao == 4:
            resultado = fn.dividir(numero1,numero2)
        
        print(f"O resultado é {resultado}")

    else:
        print("\nOpção inválida")
    
    op = input("\nFazer outra conta s / n: ").lower()

    if op != "s":
        break
