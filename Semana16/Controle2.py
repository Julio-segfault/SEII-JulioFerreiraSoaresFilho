
import matplotlib.pyplot as plt
import numpy as np
import control
import scipy.signal as signal

s = control.tf('s')
sysnum = [9]
sysdem = [1, 2, 9]
sys = control.tf(sysnum, sysdem)
ks = 1
a = 1
b = 12.29645
k=536
comp = k*(b/a)*(s+a)/(s+b)
sysid = 9/(s**2 + 2*2.198805*s + 3**2)

sysc = sys*(comp)
Tref = np.arange(0,30,0.05)
print(sys.zero())
print(sys.pole())
control.root_locus(sys)
control.root_locus(sysc)
sysfeed = control.feedback(sysc, sys2=1, sign=-1)
Time, Out = control.step_response(sys,Tref, X0=0.0)
Time2, Outc = control.step_response(sysfeed, Tref, X0=0.0)
Over = max(Out)/Out[-1]
print(Over)
Overc = max(Outc)/Outc[-1]
print(Overc)
plt.figure(figsize=(10,6), dpi=100)
plt.plot(Time, Out)
plt.plot(Time2,Outc, color='red')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
#plt.savefig('Graph1.png', dpi=100)

plt.show()