# Importando funções/ bibilotecas
from random import randint
from time import sleep

# Criando funções
def verify_number()-> int:
    """Função responsável por verificar se o número digitado pelo jogador é válido. Caso digite uma str ou um número fora do intervalo
    de 1 a 15 pede para inserir uma opção válid.

    Returns:
        int: int entre 1 e 15
    """
    
    while True:
        
        escolha = input("Adivinhe o número que estou pensando. Ele está entre 1 e 15: ")
        
        try:
            escolha = int(escolha)
        except ValueError:
            print("O número não deve ser escrito por extenso tem que ser digitado. EX: 2")
            sleep(1)
            continue
        
        if 1 <= escolha <= 15:
            return escolha
        else:
            print("O número escolhido não está entre 1 e 15. Selecione um número Válido!")
            sleep(1)
 
# check do resultado
def check_result(sorteado:int, escolha:int) -> bool:
    """Verificar se o jogador acertou o número sorteado

    Args:
        sorteado (int): Número sorteado pelo programa
        escolha (int): Número selecionado pelo jogador

    Returns:
        bool: Se o jogador acertou retorna True se errou retorna False
    """
    
    
    if sorteado > escolha:
       print(f"Não foi esse número que pensei. O número que eu pensei é maior, tente outra vez!")
       sleep(1)
       return False
    elif sorteado < escolha:
        print(f"Não foi esse número que pensei. O número que eu pensei é menor, tente outra vez!")
        sleep(1)
        return False
    else:
        return True

# Declarando variaveis
num_sorteado = randint(1,15)


# Fazendo operação do jogo
for i in range(3):
    num_escolhido = verify_number()
    
    if check_result(sorteado = num_sorteado, escolha = num_escolhido):
        print(f"Parabéns você acertou! Precisou somente de {i + 1} tentativas")
        break
    elif i < 2:
        print(f"Você tem {2 - i} tentativas restantes")
        sleep(1)

else:
    print(f"Suas tentativas acabaram! O número secreto era {num_sorteado}. Tente outra vez!")