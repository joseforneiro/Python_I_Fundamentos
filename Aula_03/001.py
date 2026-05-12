import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

nome_completo = input("Digite o seu nome completo: ")

print(len(nome_completo)) # também conta os espaços em branco
print(nome_completo.upper())
print(nome_completo.lower())
print(nome_completo.capitalize())
print(nome_completo.replace(' ', ''))

espaco = nome_completo.find(' ')
print(nome_completo[0:espaco])

print(nome_completo.split())