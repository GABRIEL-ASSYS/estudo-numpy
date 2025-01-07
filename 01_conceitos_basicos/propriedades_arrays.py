import numpy as np

# Criando um array 2D
array = np.array([[1, 2, 3],
                  [4, 5, 6]])

# Propriedades do array
print("Array:")
print(array)
print("\nForma (shape):", array.shape)
print("\nNúmero de dimensões:", array.ndim)
print("\nNúmero total de elementos:", array.size)
print("\nTipo de dados (dtype):", array.dtype)