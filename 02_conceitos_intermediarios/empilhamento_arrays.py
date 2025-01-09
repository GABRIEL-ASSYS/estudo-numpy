import numpy as np

# Criando dois arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Empilhamento vertical
vertical_stack = np.vstack((a, b))
print("Empilhamento Vertical:")
print(vertical_stack)

# Empilhamento horizontal
horizontal_stack = np.hstack((a, b))
print("\nEmpilhamento Horizontal:")
print(horizontal_stack)

# Empilhamento com `column_stack` (colunas)
column_stack = np.column_stack((a, b))
print("\nEmpilhamento em Colunas:")
print(column_stack)