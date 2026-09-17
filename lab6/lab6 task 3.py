import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

spisok = []

x = a

while x <= b:
    y = math.exp(x) / (x ** 2 + 0.11)
    spisok.append(y)
    x = x + h

print("Початковий список:")
print(spisok)

spisok.sort(reverse=True)

print("Список за спаданням:")
print(spisok)

seredyna = len(spisok) // 2

spisok1 = spisok[:seredyna]
spisok2 = spisok[seredyna:]

print("Перший список:")
print(spisok1)

print("Другий список:")
print(spisok2)