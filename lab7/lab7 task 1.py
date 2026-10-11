s = input()

suma = 0
dobutok = 1

for c in s:
    if c.isdigit():
        suma += int(c)
        dobutok *= int(c)

print(suma)
print(dobutok)