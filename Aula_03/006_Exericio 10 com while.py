import os

opcao = "sim"
while opcao == "sim":

    os.system('cls' if os.name=='nt' else 'clear') 

    salario_bruto = float(input("Digite seu salário bruto: "))
    inss = 0
    irrf = 0
    salario_base = 0
    salario_liquido = 0
    aliquota_irrf = ''

    if salario_bruto > 8475.55:
        inss = (8475.55 * 14 / 100) - 198.49
    else:
        if salario_bruto <= 1621:
            inss = salario_bruto * 7.5 / 100
        elif salario_bruto <= 2902.84:
            inss = (salario_bruto * 9 / 100) - 24.32
        elif salario_bruto <= 4354.27:
            inss = (salario_bruto * 12 / 100) - 111.40
        elif salario_bruto <= 8475.55:
            inss = (salario_bruto * 14 / 100) - 198.49

    salario_base = salario_bruto - inss

    if salario_base <= 2428.80:
        irrf = 0
        aliquota_irrf = '0.0%'
    elif salario_base <= 2826.65:
        irrf = (salario_base * 7.5 / 100) - 182.16
        aliquota_irrf = '7.5%'
    elif salario_base <= 3751.05:
        irrf = (salario_base * 15 / 100) - 394.16
        aliquota_irrf = '15.0%'
    elif salario_base <= 4664.68:
        irrf = (salario_base * 22.5 / 100) - 675.49
        aliquota_irrf = '22.5%'
    elif salario_base > 4664.68:
        irrf = (salario_base * 27.5 / 100) - 908.73
        aliquota_irrf = '27.5%'

    salario_liquido = salario_base - irrf

    print(f"\nSalário Bruto = {salario_bruto:.2f}")
    print(f"Salário Base = {salario_base:.2f}")
    print(f"Salário Líquido = {salario_liquido:.2f}")
    print(f"INSS = {inss:.2f}")
    print(f"IR = {irrf:.2f}")
    print(f"Aliquota IR = {aliquota_irrf}")

    opcao = input("Deseja executar o código novamente? (sim / não): ").lower()

print("\nObrigado por usar nosso sistema!!!")