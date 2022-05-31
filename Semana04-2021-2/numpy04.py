import numpy as np
import matplotlib.pyplot as plt

a1 = 2*np.random.randn(10000) + 10

m = np.mean(a1)
s = np.std(a1)
q = np.percentile(a1, 80)

print(m, s, q)

x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y,x)
y_int = np.cumsum(y)*(x[1]-x[0])
print(np.cumsum(np.array([1, 2, 3, 4])))

fig1 = plt.figure()

plt.plot(x,y)
plt.plot(x, dydx)
plt.plot(x,y_int)
plt.grid('True')
plt.show()

