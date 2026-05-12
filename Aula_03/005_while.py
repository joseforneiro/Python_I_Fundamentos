import os
os.system('cls' if os.name=='nt' else 'clear') 
# Todo o sistema windows tem nome nt.
# Então se for windows vai usar cls e se for linux clear

# alt + z quebra a linha quando extrapola a largura da tela.

opcao = 'sim'
while opcao == 'sim':
    print("Olá")

    opcao = input("Deseja executar o código novamente? (sim / não): ").lower()
    os.system('cls')


os.system('cls')
print("Obrigado por usar o sistema")
