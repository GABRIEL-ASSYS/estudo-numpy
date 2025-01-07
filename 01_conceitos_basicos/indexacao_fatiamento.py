import numpy as np

# Criando um array 2D
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Acessando elementos individuais
print("Elemento na posição (0, 1):", array[0, 1])  # Linha 0, Coluna 1
print("Elemento na posição (2, 2):", array[2, 2]) # Linha 2, Coluna 2

# Fatiando o array
print("\nFatiando o array:")
print("\nPrimeira linha:", array[0, :]) # Todas as colunas da linha 0
print("\nPrimeira coluna:", array[:, 0]) # Todas as linhas da coluna 0
print("\nSubmatriz (2x2):")
print(array[1:, 1:]) # Linhas 1 e 2, colunas 1 e 2