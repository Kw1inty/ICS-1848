
import matplotlib.pyplot as plt

names = []
areas = []

f = open('areas.txt', 'r', encoding='utf-8')

for line in f:
    name, area = line.strip().split(':')
    names.append(name)
    areas.append(float(area))

f.close()

plt.barh(names, areas)

plt.xlabel('Площа')
plt.ylabel('Області України')
plt.title('Площі областей України')

plt.show()
