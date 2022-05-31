import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([2,4,6,8,10])
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[1:-2])
print(a1[a1>3])

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])

firstletter_j = np.vectorize(lambda s:s[0])(names)=='J'

f= lambda s:s[0]
print(f('animal'))

print(names[firstletter_j])

print(a1%4)
i4 = a1%4==0
print(a1[i4])