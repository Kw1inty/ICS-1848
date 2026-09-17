import math

x = float(input("Введіть x: "))

if x >= 5.2:
    y = math.exp(3.27 * abs(x - 9) + 1) + x
elif x > 0.19:
    y = math.cos(x) + math.cos(x) / math.sin(x) + math.sqrt(abs(x - 7.84))
else:
    y = math.sin(abs(x - 0.7)) + 3.33 * 2 ** x

print("f(x) =", y)