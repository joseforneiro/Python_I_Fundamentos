import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print('Primeiro for: \n')
for i in range(10):
    print(i)

print('\nSegundo for: \n')
# range(inicio,fim)
for i in range(2,10): 
    print(i)

print('\nTerceiro for: \n')
# range(inicio,fim,incremento)
for i in range(0,10,2): 
    print(i)

print('\nQuarto for: \n')
# range(inicio,fim,incremento)
for i in range(10,0,-1): 
    print(i)

print('\nQuinto for: \n')
# range(inicio,fim,incremento)
for i in range(10,-1,-1): 
    print(i)