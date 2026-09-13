import math

x = float(input("Введіть x: "))

f = 2.7 * math.log(abs(math.sin(math.sqrt(x)))) - \
    8 / (math.sqrt(x + x**(1/3)) + 0.02)

print("f(x) =", f)