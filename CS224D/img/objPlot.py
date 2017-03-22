import matplotlib.pyplot as plt
import numpy as np
d = np.arange(-3, 5, 0.1)
J = [max(0, 1-i) for i in d]

line, = plt.plot(d, J, lw=2)

plt.annotate('No need to optimize further', xy=(1, 0), xytext=(2, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylim(-2,6)
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('d = s+ive - s-ive')
plt.ylabel('objective: J')
plt.savefig('ObjPlot.png')

plt.show()
