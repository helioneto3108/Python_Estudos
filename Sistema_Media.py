# Declarando variáveis e listas
#%%
nomes = ["Maria Silva",
         "João Santos",
         "Ana Oliveira",
         "Pedro Costa",
         "Juliana Pereira"]

medias = [8.9,
          7.5,
          4.2,
          1.4,
          9.5]

nota_max = 10
corte = 5

# Adicionando mais 1 na media pelo trabalho
for i in range(len(medias)):
    medias[i] += 1
    if medias[i] > nota_max:
        medias[i] = nota_max

# Exibindo as médias finais    
print(f"As médias ficaram {medias}")