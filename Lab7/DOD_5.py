import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3.16, 3.16, 0.1)

plt.plot(x)
plt.plot(2*np.sin(x))
plt.plot(2+np.sin(x))
plt.plot(np.sin(2*x))
plt.show()

