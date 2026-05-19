import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

# Tratamnuento de erros:

try:
    numero = int(input("Digite um número: "))

    print(numero)
    
except Exception as erro:
    print("Erro: ", erro)