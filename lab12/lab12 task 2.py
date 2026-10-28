import os
import random

folder = os.path.dirname(os.path.abspath(__file__))


def make_number():
    series = random.choice("AEUFQRZW")
    digits = ""
    for i in range(8):
        digits += str(random.randint(0, 9))
    voltage = random.choice([3, 6, 12])
    return series + digits + "-" + str(voltage)


N = int(input("Введіть кількість номерів N: "))

numbers = []
for i in range(N):
    numbers.append(make_number())

numbers.sort()

f = open(os.path.join(folder, "batteries.txt"), "w", encoding="utf-8")
for number in numbers:
    f.write(number + "\n")
f.close()

print("Номери записано у файл batteries.txt в порядку зростання:")
for number in numbers:
    print(number)
