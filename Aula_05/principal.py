import os
import funcoes as fn # renomeando a importação

os.system('cls' if os.name=="nt" else 'clear') # resultado se verdadeiro para a condição se não resultado para se falso

resultado = fn.somar(5,2)
print(resultado)