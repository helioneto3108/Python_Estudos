# Importando funções/ bibilotecas
from random import randint

# Sorteando o numero e declarando variavel
num_sorteado = randint(1,15)
count = 1

# Solicitando ao usuário o número que ele irá chutar
num_escolhido = input("Adivinhe o número que estou pensando. Ele está entre 1 e 15: ")

# Fazendo a operação do jogo
while True:
    
    try:
        int(num_escolhido)
    except ValueError:
        print("O número não deve ser escrito por extenso tem que ser digitado. EX: 2")
        num_escolhido = input("Selecione o número válido: ")
        continue
        
    if count >= 3  and num_escolhido != num_sorteado:
        print(f"Que pena você não adivinhou o número era {num_sorteado}")
        break 
    
    elif int(num_escolhido) > 15 or int(num_escolhido) < 1:
        num_escolhido = input("O número escolhido não está entre 1 e 15. Selecione um número válido: ")
        
    elif int(num_escolhido) > int(num_sorteado):
        num_escolhido = input(f"Não foi esse número que pensei. O número que eu pensei é menor, tente outra vez , você ainda tem mais {3 - count} tentativas: ")
        count += 1
        
    elif int(num_escolhido) < int(num_sorteado):
        num_escolhido = input(f"Não foi esse número que pensei. O número que eu pensei é maior, tente outra vez , você ainda tem mais {3 - count} tentativas: ")
        count += 1 
    
    else:
        print(f"você acertou o número, parabéns! Você so precisou de {count} tentativas")
        break