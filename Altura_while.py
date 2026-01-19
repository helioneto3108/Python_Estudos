# Declarando variaveis
soma = 0
count = 0

# Recebendo alturas e somando
while count < 4:
    altura = int(input("Digite a sua altura em cm: "))
    soma += altura
    count += 1

# Exibindo a soma
print(f"A soma das alturas deu {soma} cm")