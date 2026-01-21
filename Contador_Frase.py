# Declarando variaveis
frases = list()

# Solicitando ao usuário frases
while True:
    oracao = input("Digite uma frase que deseja armazenar e se quiser para aperte enter:\n").strip().capitalize()
    frases.append(oracao)
    
    if oracao == "":
        break
    
# exibindo frases e qtde de vezes que foi escrita
for i in frases:
    print(f"A frase {i} foi repitida {frases.count(i)} vezes")
    while frases.count(i) > 0:
        frases.remove(i) # Feito para repetir a frase somente 1 vez