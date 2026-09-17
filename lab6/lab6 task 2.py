import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

while x <= b:
    y = math.exp(x) / (x ** 2 + 0.11)
    print("x =", x, " y =", y)
    x = x + h