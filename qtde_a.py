# Declarando variaveis
count = 0

# Solicitando texto
texto = input("Digite a frase que quer saber quantos As possui nela:\n")

# Verificando a quantidade de As
for i in texto:
    if i == "A" or i == "a":
        count += 1

# Exibindo resposta ao cliente
print(f"A quantidade de As presente na frase é {count}")