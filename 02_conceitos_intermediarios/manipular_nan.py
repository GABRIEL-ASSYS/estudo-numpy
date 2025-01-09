import numpy as np

# Criando um array com valores NaN
array = np.array([1, 2, np.nan, 4, 5, np.nan])

# Verificar onde estão os NaN
print("Array Original:")
print(array)
print("\nMáscara de NaN:", np.isnan(array))

# Substituir NaN por zero
array_sem_nan = np.nan_to_num(array, nan=0)
print("\nArray com NaN Substituído por Zero:")
print(array_sem_nan)

# Calcular média ignorando NaN
media = np.nanmean(array)
print("\nMédia Ignorando NaN:", media)