import numpy as np

sites = {"google.com", "github.com", "python.org", "sute.edu.ua", "telegram.org"}

T = tuple(sites)
L = list(sites)
A = np.array(list(sites))

print("Множина у рядок:")
print(sites)
print("Множина в стовпчик:")
for elem in sites:
    print(elem)

print("Кортеж:", T)
print("Список:", L)
print("Масив рядків:", A)