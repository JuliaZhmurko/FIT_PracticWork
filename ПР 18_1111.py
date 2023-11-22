import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,5)
y=np.exp(x)*np.sin(x)
plt.plot(x, y, color='yellow', linestyle='-.', label='y=np.exp(x)*np.sin(x)')
plt.xlabel('Вісь х')
plt.ylabel('Вісь y')
plt.title('Графік функції')
plt.legend()
plt.savefig("exponent1.png")
plt.show()
