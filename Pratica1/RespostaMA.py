"""
Esse codigo simula o comportamento pendulo invertido
"""
# Importando bibliotecas
from scipy.integrate import odeint
from numpy import zeros, ones, arange, pi, sin, cos
import matplotlib.pyplot as plt


# Definindo dinamica da planta
# noinspection PyTypeChecker
def din_pend(y, t, u):
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
u = zeros(kend)  # % de duty cycle

thetap = zeros(kend)  # velocidade angular do motor
theta = zeros(kend)  # posicao angular real do motor
e = zeros(kend)  # erro de rastreamento

# Referencia do theta e da entrada
theta_ref = 58.358*pi/180 + zeros(kend)  # rad. Em relacao a theta = pi

u_ref = p*l1*sin(theta_ref)/l2

# Condicao inicial
theta[0] = 0*pi/180  # rad  - Inicialmente na pos. de equilibrio

# Loop
for k in range(kend-1):

    # Degrau de referencia
    if k*Ta > 1:
        u[k] = u_ref[k]

    # Calculo do erro de rastreamento

    # Calculo da acao de controle

    # Limitando acao de controle

    # Evoluindo a din. da planta
    x0 = [theta[k], thetap[k]]   # condicao inicial
    sol = odeint(din_pend, x0, [0.0, Ta], args=(u[k],))
    theta[k + 1] = sol[:, 0][-1]
    thetap[k+1] = sol[:, 1][-1]


# Plotando resultados
fig1 = plt.figure()
plt.plot(arange(0, Tsim, Ta), theta*rad2deg, lw=2, label=r'\theta (deg)')
plt.plot(arange(0, Tsim, Ta), theta_ref*rad2deg, lw=2, label=r'\theta_{ref} (deg)')
plt.xlabel('Tempo (s)')
plt.legend()
plt.grid(True)

fig2 = plt.figure()
plt.plot(arange(0, Tsim-Ta, Ta), u[0:-1], lw=2)
plt.xlabel('Tempo (s)')
plt.ylabel(r'u (N)')
plt.grid(True)


plt.show()
