# Declarando variaveis
cesta = {
    "frutas": ["Maça", "Banana", "Uva", 
               "Pera", "Laranja", "Limão",
               "Goiaba", "Abacaxi", "Jaca"],
    
    "Preço": [1.5, 2.75, 1.9,
              1.25, 0.65, 1.25,
              2.15, 3.20, 5.8]
}

soma = 0

# Entrada da fruta pelo cliente
pedido = input("Digite o nome da fruta que você deseja: ").strip().capitalize()

# Operacionalizando sistema
while True:
    if pedido == "Fim":
        break
    
    elif pedido in cesta["frutas"]:
        qtde_fruta = int(input("Quantas frutas dessa voce deseja?\n"))
        indice = cesta["frutas"].index(pedido)
        soma += qtde_fruta * cesta["Preço"][indice]
        pedido = input("Digite fim se quiser finalizar ou digite o nome de outra fruta para comprar: ").strip().capitalize()
        
    else:
         pedido = input("Não encontramos essa fruta, digite outra fruta ou corrija o nome da fruta desejada. Se quiser finalizar digite fim: ").strip().capitalize()

    
# %%
#Exibindo valor a ser pago
print(f"A soma das frutas deu {soma:.2f}")