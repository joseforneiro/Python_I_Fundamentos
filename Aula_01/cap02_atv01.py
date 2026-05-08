# Primeiro modo de fazer:

# numero1 = input("Digite o primeiro número da soma: ")
# numero2 = input("Digite o segundo número da soma: ")

# **********************************************
# Conversão utilizando float:
# soma = float(numero1) + float(numero2)

# print(f"O resultado da soma é {soma:.2f}")
# O .2f quer dizer duas casas decimais.

# **********************************************
# Conversão utilizando int:
# soma = int(numero1) + int(numero2)

# print(f"O resultado da soma é {soma}")


# Segundo modo de fazer:

import os # os é de sistema operacional
os.system('cls') # Limpa a tela antes de rodar o código

numero1 = float(input("Digite o primeiro número da soma: "))
numero2 = float(input("Digite o segundo número da soma: "))

soma = numero1 + numero2

print(f"O resultado da soma é {soma:.2f}")