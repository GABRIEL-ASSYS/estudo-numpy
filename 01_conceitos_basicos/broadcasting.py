import numpy as np

# Criando um array 2D (2x3)
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

# Criando um array 1D (tamanho 3)
array_1d = np.array([10, 20, 30])

# Broadcasting: Adicionando um array 1D a um array 2D
# O NumPy "expande" o array 2D para que tenha o mesmo formato do 2D
result = array_2d + array_1d

print("Array 2D:")
print(array_2d)
print("\nArray 1D:")
print(array_1d)
print("\nResultado do Broadcasting (Array 2D + Array 1D):")
print(result)

# Broadcasting com escalares
# O escalar é aplicado a todos os elementos do array
result_scalar = array_2d * 2
print("\nResultado do Broadcasting com Escalar (Array 2D * 2):")
print(result_scalar)