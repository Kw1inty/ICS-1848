
import numpy as np

n = int(input("Введіть розмір масиву: "))

A = np.zeros((n, n), dtype=int)

k = 1

for j in range(n - 1, -1, -1):
    for i in range(n):
        A[i][j] = k
        k += 1

print("Масив A:")
print(A)
