# %%
# Lendo Arquivo
arq = "dados.csv"
with open(arq) as open_file:
    raw_data = open_file.readlines()
    
raw_data
# %%
# Pegando as chaves pro dic
chaves = raw_data[0].replace("\n", "").split(";")
chaves
# %%
# Criando dict
data = dict()
data
# %%
# Criando as chaves do Dict
for i in chaves:
    data[i] = []

data
# %%
# Populando Dict
for i in raw_data[1:]:
    valores = i.replace("\n", "").split(";")
    
    for i in range(len(valores)):
        data[chaves[i]].append(valores[i])

data
# %%
