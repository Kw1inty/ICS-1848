import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

n = int((b - a) / h)

for i in range(n + 1):
    x = a + i * h
    y = math.exp(x) / (x ** 2 + 0.11)
    print("x =", x, "y =", y)