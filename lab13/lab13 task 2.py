import random
from nat_module import Nat

numbers = []
for i in range(5):
    numbers.append(Nat(random.randint(1, 100)))

for n in numbers:
    print("Число:", end=" ")
    n.DisplayValue()
    print("Дільники:", end=" ")
    n.DisplayDivs()
    print()
