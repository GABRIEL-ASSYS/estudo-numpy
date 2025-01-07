import numpy as np

# Criando array a partir de uma lista simples
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1D (a partir de lista):", array_1d)

# Criando um array 2D a partir de uma lista de listas
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray 2D (a partir de lista de listas):")
print(array_2d)

# Criando arrays pré-definidos (zeros, uns, valores aleatórios)
zeros = np.zeros((2, 3)) # Array de zeros com 2 linhas e 3 colunas
ones = np.ones((3, 2)) # Array de uns com 3 linhas e 2 colunas
random_values = np.random.random((2, 2)) # Array de valores aleatórios

print("\nArray de Zeros:")
print(zeros)
print("\nArray de Uns:")
print(ones)
print("\nArray de Valores Aleatórios:")
print(random_values)

# Criando um array com valores espaçados uniformemente
linear_space = np.linspace(0, 10, 5) # De 0 a 10, com 5 valores
print("\nArray com valores espaçados uniformemente (linspace):", linear_space)