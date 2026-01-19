# Declarando variaveis
soma = 0
qtde_pessoas = 4

# Pedindo as 4 alturas em m
for i in range(qtde_pessoas):
    altura = float(input("Digite sua altura em m: "))
    soma += altura

# Exibindo a soma das alturas
print(f"A soma das alturas dá {soma:.2f}m")