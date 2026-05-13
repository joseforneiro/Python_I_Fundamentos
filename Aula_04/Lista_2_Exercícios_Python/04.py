import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Mostre apenas pares:\n")
for i in range(1,101):
    if i % 2 != 0:
        continue
    print (i)