import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Login simples:\n")

senha = 'admin123'
entrada = ''

while entrada != senha:
    entrada = input("Digite a senha: ")

print("\nLogin realizado")