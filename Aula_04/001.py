import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

while True:
    print("Loop rodando!!!")

    numero = int(input("\nDigite um número: "))
    if numero == 10:
        break # O break para o loop


for i in range(1,11):
    if i == 5:
        continue # Quando o i for igual a 5 ele não irá printar.
        # Ele irá desconsiderar o 5, ou seja, ele vai para o próximo valor de i
    print (i)