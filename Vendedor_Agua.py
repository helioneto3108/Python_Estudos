# Programa para vender agua
# %%
# Definindo variáveis
qtde_Gas = 0
qtde_Natural = 0
# %%
# Mensagem Inicial
Msg_Inicial = """Olá seja bem vindo! Qual das seguintes opções de água você deseja comprar?
(1) Água Mineral Natural
(2) Água Mineral Com Gás
(3) Ambas"""
print(Msg_Inicial)
# %%
# Declarando variáveis
natural = 1.5
Gas = 2.5
# %%
# Solicitando input do tipo de agua do cliente
selecao = int(input("Digite o número referente a opção que deseja: "))
# %%
# Solicitando quantidade
if selecao == 3:
    qtde_Natural = float(input("Digite o número da quantidade de garrafa de água natural que deseja\n"))
    qtde_Gas = float(input("Digite o número da quantidade de garrafa de água com gás que deseja\n"))
elif selecao == 2:
    qtde_Gas = float(input("Digite o número da quantidade de garrafa de água com gás que deseja\n"))
else:
    qtde_Natural = float(input("Digite o número da quantidade de garrafa de água natural que deseja\n"))
# %%
# Fazendo o calculo do total
total = (natural * qtde_Natural) + (Gas * qtde_Gas) 
# %%
# Exibindo total que deve pagar
print(f"Muito obrigado por escolher a gente! O valor total deu R${total:.2f}, volte sempre!")