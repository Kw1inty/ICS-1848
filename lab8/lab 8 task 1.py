
from array import *

masiv = array('i', [])

for i in range(10):
    x = int(input("Введіть число: "))
    masiv.append(x)

ser = sum(masiv) / len(masiv)

rez = array('i', [])

for x in masiv:
    if x <= ser:
        rez.append(x)

print("Середнє арифметичне:", ser)
print("Отриманий масив:", rez)
