import os
os.system('cls')

media = 0
maior_nota = -1
menor_nota = 11

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    media += nota

    if nota > maior_nota:
        maior_nota = nota
    
    if nota < menor_nota:
        menor_nota = nota
    
print(f"Média de notas = {media / 5:.0f}")
print(f"A maior nota é = {maior_nota}")
print(f"A menor nota é = {menor_nota}")

# A minha solução ficou melhor.