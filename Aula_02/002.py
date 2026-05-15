import os
os.system('cls' if os.name=='nt' else 'clear') # resultado se verdadeiro para a condição se não resultado para se falso
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

centimetros = float(input("Digite o valor em cm: "))
print("\nEscolha uma opção para conversão:")
opcao = input("1 - polegadas \n2 - Pés \n3 - Jardas \nDigite a opção: ")

if opcao == "1":
    resultado = centimetros / 2.54
elif opcao == "2":
    resultado = centimetros / 30.48
elif opcao == "3":
    resultado = centimetros / 91.44
else:
    resultado = "Digite uma opção válida"

print(f"\nResultado = {resultado}")