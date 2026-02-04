# %%
# Importando bibilotecas
import requests

# %%
# Recebendo CEP
cep = input("Digite o SOMENTE o número do CEP que está buscando (EX: 12345678):\n")

while True:
    try:
        cep = int(cep)
        break
    except ValueError:
        cep = input("Você deve digitar somente números\n")    

# %%
# Fazendo requisição para API

ulr = "https://viacep.com.br/ws/{cep}/json/"

requisicao = requests.get(ulr.format(cep = cep))

if requisicao.status_code == 200:
    dict_cep = requisicao.json()

else:
    print("O CEP não foi encontrado, talvez você tenha digitado errado")
    exit()
    
# %%
# Exibindo informações na tela
texto = f"""O CEP {cep} é referente as seguintes informações:
Cidade: {dict_cep["localidade"]}
Bairro: {dict_cep["bairro"]}
Estado: {dict_cep["estado"]}
Regiao: {dict_cep["regiao"]}
"""
print(texto)
# %%
