import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.02)

op1 = 2*a1
op2 = 1/a1
op3 = a1>4
op4 = 1/a1 + a1 + 2
x = np.linspace(0, 1 , 100)
y = x**2

fig1 = plt.figure()
plt.plot(x,y)
plt.grid(True)

fig2 = plt.figure()
plt.hist(a4)



def f(x):
    return x**2 * np.sin(x)/np.exp(-x)

x1 = np.linspace(0,10,100)
y1 = f(x1)

fig3 = plt.figure()
plt.plot(x1,y1)

plt.show()