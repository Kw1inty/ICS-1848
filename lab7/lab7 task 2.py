
import random

n = int(input("Введіть кількість рядків: "))

for i in range(n):
    s = input("Введіть рядок: ")

    k = len(s) // 3

    parts = [s[:k], s[k:2*k], s[2*k:]]
    random.shuffle(parts)

    print("Результат:")
    for part in parts:
        print(part)
