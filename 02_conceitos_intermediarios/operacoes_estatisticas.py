import numpy as np

# Criando um array 2D
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array Original:", array)

# Média de todos os elementos
media = np.mean(array)
print("\nMédia de Todos os Elementos:", media)

# Mediana
mediana = np.median(array)
print("\nMediana:", mediana)

# Desvio padrão
desvio_padrao = np.std(array)
print("\nDesvio Padrão:", desvio_padrao)

# Soma e produto ao longo de eixos
soma_colunas = np.sum(array, axis=0) # Soma por coluna
soma_linhas = np.sum(array, axis=1) # Soma por linha
print("\nSoma por Colunas:", soma_colunas)
print("\nSoma por Linhas:", soma_linhas)