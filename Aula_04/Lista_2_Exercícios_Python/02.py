import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Contagem regressiva:\n")
for i in range(20,-1,-1):
    print(i)