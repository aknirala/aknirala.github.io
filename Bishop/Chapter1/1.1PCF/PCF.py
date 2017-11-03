import numpy as np
import matplotlib.pyplot as plt

points = 10
x = np.arange(0, 2*np.pi, 2*np.pi/points)
t = np.sin(x) + np.random.normal(0, 0.3, len(x))

xsin = np.arange(0, 2*np.pi, 0.1)
tsin = np.sin(xsin)

plt.plot(x, t, 'ro')
plt.plot(xsin, tsin)
plt.xlabel('x')
plt.ylabel('t')
plt.axhline(y=0, color='k')
plt.show()
