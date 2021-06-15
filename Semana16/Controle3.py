import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *

sysnum = [9]
sysdem = [1, 2, 9]
sys = tf(sysnum, sysdem)

Ts = 0.01
sysd = c2d(sys, Ts, method='tustin')

#Kp =2000000, Ki = 20000 e Kd = 40 quebra o programa
Kp=500
Ki=50
Kd =20
P = tf([Kp], [1], Ts)
I = (Ki*Ts/2)*tf([1,1],[1,-1],Ts)
D = (2*Kd/Ts)*tf([1,-1],[1, 1], Ts)

Cz = P + I + D

sysf = feedback(Cz*sysd)
Out, Time = step(sysf)

Over = max(Out)/Out[-1]
print(Over)

plt.figure(figsize=(10,6), dpi=100)
plt.plot(Time, Out)
plt.grid()
plt.show()




