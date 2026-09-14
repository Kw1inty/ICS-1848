import math


def calculate_f(x):
    return 2.7 * math.log(abs(math.sin(math.sqrt(x)))) - \
        8 / (math.sqrt(x + x**(1/3)) + 0.02)


x = float(input("Введіть x: "))2

print("f(x) =", calculate_f(x))