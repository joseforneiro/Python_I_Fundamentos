import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Soma dos números:\n")
soma = 0
for i in range(1,101):
    soma += i
print (f"Total = {soma}")