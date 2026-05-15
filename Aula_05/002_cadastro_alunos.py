import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

lista = []

while True:
    nome = input("Digite um nome: ").upper()
    if not nome in lista:
        lista.append(nome)
    else:
        print("Esse nome já foi adicionado!!!")

    op = input("\nDeseja incluir outro nome na lista? s / n ").lower()
    if op == "n":
        break

for nome in lista:
    print(nome)

# ou no caso de eu também querer saber o index:

for i,nome in enumerate(lista):
    print(f"I: {i} / Nome: {nome}")


busca = input("\nDigite um nome que queira buscar na lista: ").upper()
if busca in lista:
    print("O nome foi encontrado!!!")
else:
    print("O nome não foi encontrado!!!")