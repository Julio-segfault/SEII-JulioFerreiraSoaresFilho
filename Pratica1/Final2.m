clear all
close all
clc

pkg load control;

%Parâmetros do sistema

g = 9.81;
l1 = 1.2 ; 
l2 = 0.75;
m = 2.5;
p = m*g;
J = 3e-3;
ua = 0.08;

%Cálculo das constantes
Theta_barra = 30*pi/180;
u_barra = p*l1*sin(Theta_barra)/l2;
b1 = l2/J;
a1 = ua/J;
a2 = p*l1*cos(Theta_barra)/J;

s = tf('s');

Theta = (b1)*1/(s^2 + a1*s + a2);
pTheta = pole(Theta);

disp ('Pólos de malha aberta de theta: '), disp (pTheta);

%Diagrama de Bode para achar wb
[mag, phase, wout] = bode(Theta);

%indice de wb
indice = find((mag/mag(1)) < 0.707);
wb = wout(indice(1));
wmin = 40*wb;
Tmax = 2*pi/wmin;

disp('Tempo de amostagem máximo: '), disp(Tmax); 

%Tempo de amostragem
Ta = 0.001;
disp ('Tempo de amostragem escolhido: '), disp (Ta);


a21 = -a2 ;
a22 = -a1;

b21 = b1;


%Matrizes do sistema
A = [0, 1;
     a21, a22];
     
B = [0;
     b21];

C = [1, 0];

D = 0;

T = Ta;

%Cálculo da matriz de transição
O = e^(A*T);


sz = size(A);
P = eig(A);

nn = 20
%Cálculo por meio de série da matriz de transição
Oc = zeros(sz);
for ii=0:nn
  Oc = Oc + (A^ii)*(T^ii)/factorial(ii);
  endfor

  Oc;

%Cálculo da matriz gama  
Ga = zeros(sz);
for ii=0:nn
  Ga = Ga + (A^ii)*(T^(ii+1))/factorial(ii+1);
endfor
G = Ga*B;

%Sistema discreto no espaço de estados
Sys = ss(Oc, G, C, D, T);

%Cálculo dos polos do sistema discreto
Pd = eig(Oc);

Obser1 = [C; C*O]
Dob1 = det(Obser1)

Cntr1 = [B O*B]
Dctr1 = det(Obser1)

z = tf('z', T);

c1 = 1;
c2 = -1.969558964;
c3 = 0.970445531;

Car = (c1*z^2 + c2*z + c3);

Kk = acker(Oc, G, zero(Car));

disp('Vetor de ganhos: '), disp (Kk);


pe = [0.8, 0.8];
Kep = acker(Oc', C', pe)
Kec = inv(Oc)*(Kep')

N  = [Oc G; C D];
Ni = inv(N);
Nc = [0; 0; 1];

Nxu = Ni*Nc
Nx = Nxu(1:2, 1)
Nu = Nxu(3,1)

Car2 = (z - 0.71)*Car;

Ze = [0; 0];
Oe = [1 T*C; Ze Oc];
G2 = [0; G];

K2 = acker(Oe, G2, zero(Car2))

return