
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.figure(figsize=(8,4), dpi=200)

plt.plot(x, y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

#plt.plot(x, y, 'b^--',  label='2x')
#fmt = '{color}{marker}{line}'

x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')
plt.plot(x2[5:], x2[5:]**2, 'r--')

plt.title('Our first Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis', fontdict={'fontname': 'Arial Black'})
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])

plt.legend()

plt.savefig('mygraph.png', dpi=200)

plt.show()