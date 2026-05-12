import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

# print(f"{i:>4}") alinha da esquerda para a direita ocupando 4 casas
# print(f"{i:<4}") alinha da direita para a esquerda ocupando 4 casas
# print(f"{i:^4}") alinha ao centro ocupando 4 casas

print("Multitabuada - tabuada de 1 ate o 10:\n")
for i in range (1,11):
    print(f"{i:>4} {i*2:>4}  {i*3:>4} {i*4:>4} {i*5:>4} {i*6:>4} {i*7:>4} {i*8:>4} {i*9:>4} {i*10:>4} ")

# Fazendo a mesma tabuada só que com for aninhado
print("\nMultitabuada - tabuada de 1 ate o 10:\n")

for i in range(1,11):
    linha = f"{i:>4}"
    for ii in range(2,11):
        linha += f"{ii*i:>4}"
    print(linha)