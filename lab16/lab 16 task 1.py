
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100)
y = np.sin(np.pi + x) + 0.1 * np.cos(x)

plt.plot(x, y, color='cyan', linestyle='-', marker='s',
         label='sin(pi+x)+0.1*cos(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції')
plt.grid(True)
plt.legend()

plt.savefig('picture.png', dpi=300)
plt.show()
