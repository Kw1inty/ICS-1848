import math

a = float(input("Введіть a: "))
x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = float(input("Введіть z: "))

L = 6 * a * x**3 + math.sin(y) * math.cos(z) + math.tan(x + math.pi / 3)

print("L =", L)