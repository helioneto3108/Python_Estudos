# Declarando variaveis
total = 0

# Input de dados do cliente
while True:
    saldo = input("Insira o saldo que deseja colocar na sua conta:\nR$")
    
    if saldo == "":
        break
    
    total += float(saldo)

# Exibindo o saldo do cliente
print(f"O saldo inserido foi de {total:.2f}")