import numpy as np

# Criando um array 1D
array = np.array([1, 2, 3, 4, 5, 6])
print("Array inicial:")
print(array)

# Redimensionar para 2x3
array_2x3 = array.reshape(2, 3)
print("\nArray Redimensionado (2x3):")
print(array_2x3)

# Transformar para 1D novamente
array_flat = array_2x3.flatten()
print("\nArray Transformado em 1D:")
print(array_flat)

# Adicionar uma nova dimensão (3D)
array_3d = array_2x3[:, :, np.newaxis]
print("\nArray com Nova Dimensão (3D):")
print(array_3d)