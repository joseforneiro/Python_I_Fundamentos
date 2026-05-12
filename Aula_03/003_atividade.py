import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

multiplicador = int(input("Digite um número: "))
for i in range(1,11):
    print(f"{multiplicador} * {i} = {multiplicador * i}")