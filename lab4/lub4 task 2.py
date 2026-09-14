import math


def calculate_l(a, x, y, z):
	return 6 * a * x**3 + math.sin(y) * math.cos(z) + math.tan(x + math.pi / 3)


a = float(input("Введіть a: "))
x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = float(input("Введіть z: "))

print("L =", calculate_l(a, x, y, z))