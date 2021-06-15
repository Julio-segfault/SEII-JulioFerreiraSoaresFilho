import numpy

n = []
x = []
x1 = []
y = []
y1 = []
z = []
z1 = []
u = []

#Inicialização. Criação dos vetores representando os sinais.
#As últimas 10 posições são para representação dos valores negativos
for tt in range(0, 31):
    print(tt)
    if tt < 21:
        n.append(tt)
        u.append(1)
    else:
        n.append(tt - 31)
        u.append(0)
    x.append(0)
    x1.append(0)
    y.append(0)
    y1.append(0)
    z.append(0)
    z1.append(0)

x1[1] = 1


for k in range (1, 21):
    x[k] = 2*k - 1
    if k > 1:
        x1[k] = x1[k-1] + 2*u[k-2]

    y[k] = x[k] + y[k-2]
    y1[k] = k + y[k-1]

    z[k] = y[k] + y[k-1]
    z1[k] = x[k] + z1[k-1]


print(n)
print(x)
print(x1)
print(y)
print(y1)
print(z)
print(z1)
