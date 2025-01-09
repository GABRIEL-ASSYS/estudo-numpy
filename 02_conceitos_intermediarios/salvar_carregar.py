import numpy as np

# Criando um array
array = np.array([[1, 2, 3], [4, 5, 6]])
print("Array original:")
print(array)

# Salvar o array em arquivo .npy
np.save('array_salvo.npy', array)
print("\nArray salvo como 'array_salvo.npy'.")

# Carregar o array salvo
array_carregado = np.load('array_salvo.npy')
print("\nArray Carregado do Arquivo:")
print(array_carregado)

# Salvar o array como um arquivo de texto
np.savetxt('array_salvo.txt', array, delimiter=',')
print("\nArray salvo como 'array_salvo.txt'.")

# Carregar o array de um arquivo de texto
array_txt = np.loadtxt('array_salvo.txt', delimiter=',')
print("\nArray Carregado do Arquivo de Texto:")
print(array_txt)