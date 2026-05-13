import os
os.system('cls')

numero = int(input("Digite um número: "))
soma = 0

while numero > 0:
    soma += numero % 10 # Divisão por 10 e pegando somente o resto (35 / 10 = 3,5 -> O resto sempre vai ser o último digito)
    numero = numero // 10 # Divisão por 10 e pegando somente a parte inteira do número (O inteiro de 35 / 10 = 3)

print(soma)

# 3521 % 10 = 1 (352,1)
# 3521 // 10 = 352