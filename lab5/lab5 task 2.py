x1 = float(input("Введіть x точки A: "))
y1 = float(input("Введіть y точки A: "))

x2 = float(input("Введіть x точки B: "))
y2 = float(input("Введіть y точки B: "))

x3 = float(input("Введіть x точки C: "))
y3 = float(input("Введіть y точки C: "))

a = abs(x1) + abs(y1)
b = abs(x2) + abs(y2)
c = abs(x3) + abs(y3)

if a >= b and a >= c:
    print("Точка A має найбільшу суму")
elif b >= a and b >= c:
    print("Точка B має найбільшу суму")
else:
    print("Точка C має найбільшу суму")