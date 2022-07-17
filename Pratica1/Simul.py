"""
Esse codigo simula o comportamento pendulo invertido
"""
# Importando bibliotecas
from scipy.integrate import odeint
from numpy import zeros, arange, pi, sin, cos, random
import matplotlib.pyplot as plt


# Definindo dinamica do sistema
def din_sis(y, t, u):
    # Parametros da planta
    m = 2.5 # kg
    J = 0.003
    l1 = 1.2
    l2 = 0.75
    ua = 0.08
    g = 9.81  # m/s^2
    p = m*g

    x1, x2 = y

    b1 = l2*u/J
    a1 = -p*l1*sin(x1)/J
    a2 = -ua*x2/J

    # Dinamica do pendulo
    x1p = x2
    x2p = b1 + a1 +a2

    return [x1p, x2p]


# Variaveis auxiliares
deg2rad = pi/180.
rad2deg = 180./pi

m = 2.5 # kg
J = 0.003
l1 = 1.2
l2 = 0.75
ua = 0.08
g = 9.81  # m/s^2
p = m*g

# Parametros de simulacao
Ta = 0.001
Tsim = 2  # tempo de simulacao
kend = int(Tsim/Ta)

# scopes
u = zeros(kend)  # acao de controle
u_ref = zeros(kend)
phip = zeros(kend)  # velocidade angular
phi = zeros(kend)  # posicao angular
x1e_c = zeros(kend)  # estado x1 corrigido
x2e_c = zeros(kend)  # estado x2 corrigido
x1e_p = zeros(kend)  # estado x1 predito
x2e_p = zeros(kend)  # estado x2 predito
xi = zeros(kend)
n = zeros(kend)  # ruido de medida em theta
e = zeros(kend)
r = zeros(kend)

Kep1 = 0.36531
Kep2 = 20.79009
Kec1 = 0.3427
Kec2 = 24.40297

Ki = 1042.929
K1 = 4.8995
K2 = 1.1575

# Condicao inicial
phi[0] =0 * pi / 180  # rad

# Loop
for k in range(kend - 1):
    if k*Ta > 1:
        r[k] = 30*deg2rad
    # Fase de correcao do estimador
    x1e_c[k] = x1e_p[k] + Kec1 * (phi[k] - x1e_p[k])
    x2e_c[k] = x2e_p[k] + Kec2 * (phi[k] - x1e_p[k])

    # Calculo da acao de controle
    u[k] = K1 * (r[k] - x1e_c[k]) - K2 *x2e_c[k] - Ki * xi[k]

    # Limitando acao de controle (saturacao)
    u[k] = min(u[k], 50)  # sup
    u[k] = max(u[k], -50)  # inf

    # Evoluindo a din. da planta
    x0 = [phi[k], phip[k]]  # condicao inicial
    sol = odeint(din_sis, x0, [0.0, Ta], args=(u[k],))
    n[k] = 0 # ruido de medida
    phi[k + 1] = sol[:, 0][-1] + n[k]  # estado real x1
    phip[k + 1] = sol[:, 1][-1]  # estado real x2
    e[k] = -r[k] + phi[k]
    xi[k + 1] = xi[k] + Ta * e[k]

    # Estimador de estados - fase de predicao
    x1 = [x1e_c[k], x2e_c[k]]  # condicao inicial
    sol = odeint(din_sis, x1, [0.0, Ta], args=(u[k],))
    x1e_p[k + 1] = sol[:, 0][-1] + n[k]  # estado real x1
    x2e_p[k + 1] = sol[:, 1][-1]  # estado real x2

# Plotando resultados
fig1 = plt.figure()
plt.plot(arange(0, Tsim, Ta), x1e_c * rad2deg, lw=2, label=r'x_{1,e} (deg)')
plt.plot(arange(0, Tsim, Ta), phi * rad2deg, lw=2, label=r'\theta (deg)')
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)

fig2 = plt.figure()
plt.plot(arange(0, Tsim, Ta), x2e_c * rad2deg, lw=2, label=r'x_{2,e} (deg/s)')
plt.plot(arange(0, Tsim, Ta), phip * rad2deg, lw=2, label=r'\theta (deg/s)')
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)

fig3 = plt.figure()
plt.plot(arange(0, Tsim - Ta, Ta), u[0:-1], lw=2)
plt.xlabel('Tempo (s)')
plt.ylabel(r'u (m/s^2)')
plt.grid(True)

#v = phip - x2e_p
v = xi
fig4 = plt.figure()
plt.plot(arange(0, Tsim - Ta, Ta), v[0:-1], lw=2)
plt.xlabel('Tempo (s)')
plt.ylabel(r'u (m/s^2)')
plt.grid(True)


plt.show()