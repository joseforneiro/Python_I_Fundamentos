import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Folha de pagamento")

salario = float(input("Digite o seu salário: "))
inss = 0
# Calculo do desconto do INSS:

if salario >= 0 and salario <= 1621:
    porcent = 0.075
    valor = 0
elif salario >= 1621.01 and salario <= 2902.84:
    porcent = 0.09
    valor = 24.32
elif salario >= 2902.85 and salario <= 4354.27:
    porcent = 0.12
    valor = 111.40
elif salario <= 8475.55:    
    porcent = 0.14
    valor = 198.49
else:
    inss = 8475.55 * 0.14 - 198.49

if(inss == 0):
    inss = (salario * porcent) - valor

salario_base = salario - inss

# Cálculo do Imposto de Renda:

if salario_base <= 2428.8:
    alicota = 0
    deducao = 0
elif salario_base >= 2428.81 and salario_base <= 2826.65:
    alicota = 0.075
    deducao = 182.16
elif salario_base >= 2826.66 and salario_base <= 3751.05:
    alicota = 0.15
    deducao = 394.16
elif salario_base >= 3751.06 and salario_base <= 4664.68:
    alicota = 0.225
    deducao = 675.49
else:
    alicota = 0.275
    deducao = 908.73

porcent_ir = alicota * 100
valor_ir = (salario_base * alicota) - deducao
salario_liquido = salario_base - valor

print(f"\nSalário Bruto: {salario}")
print(f"Salário Base: {salario_base}")
print(f"INSS: {inss:.2f}")
print(f"%IR: {porcent_ir}%")
print(f"Valor IR: {valor_ir}")
print(f"Salário Líquido: {salario_liquido}")