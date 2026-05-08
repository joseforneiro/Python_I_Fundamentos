import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

print("Verificação de aprovação\n")
nota = float(input("Digite a nota de 0 a 10: "))

if nota >= 7 and nota <= 10:
    resultado = "Aprovado"
elif nota >= 5 and nota <= 6.9:
    resultado = "Recuperação"
elif nota < 5 and nota >= 0:
    resultado = "Reprovado"
else:
    resultado = "Nota inválida"

print(f"\n{resultado}")