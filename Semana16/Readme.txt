Decidi por criar este arquivo separado para evitar que o código ficasse poluído com comentários.

1. No exercício foi pedido para apresentar as saídas das sequências dadas a partir dos valores iniciais e equações de diferenças.
Considerando que só estou interessado na quantidade de pontos, posso modelar cada sequência em função de sua posição como equações de diferenças lineares de coeficientes constantes (LCCDEs).
A forma geral é: y(n) = E[a(k)x(n-k)] + E[b(k)y(n-k)], onde E representa o sinal de somatório.
Cada sequência pode ser representada de várias formas. Sendo n a posição na sequência a partir do valor 1:

a. Chamaremos este primeiro sinal resultante de x(n). Existem várias representações dependendo do que é considerado como o sinal de entrada do sistema.
	Considerando  n = n para n > 0 (ou n = n*u(n)) como o sinal de entrada:
	x(n) = n + (n-1) = 2n -1
	Considerando uma entrada degrau u(n) e x(1) = 1:
	x(n) = x(n-1) + 2*u(n-2)
	Com m = n-1, x(m = 0) = 1, para m maior-igual a zero temos:
	x(m + 1) = x(m) + 2*u(m - 1)

b. Chameremos este sinal resultante de y(n).
	Considerando o sinal x(n) do item a como o sinal de entrada:
	y(n) = x(n) + y(n-2)
	y(n) = (2n-1) + y(n-2)
	Considerando n = n como sinal de entrada:
	y(n) = n + y(n-1)

c. Chamaremos este sinal resultante de z(n).
	Sendo y(n) o sinal de entrada, com y(-2) = 0 e y(-1) = 0 (apenas um destes valores é necessário dependendo da representação):
	z(n) = y(n) + y(n-1) = 2*y(n) - n = 2*y(n - 1) + n
	z(n) = x(n) + y(n-2) + y(n-1)
	z(n) = x(n) + (n-1) + 2*y(n-2) = (3n - 2) + 2*y(n - 2)
	Sendo x(n) o sinal de entrada:
	z(n) = x(n) + z(n - 1)
	Sendo n = n como sinal de entrada:
	z(n) = n + (n - 1) + z(n-1) = 2n - 1 + z(n-1)

2. O compensador foi projetado usando o método do lugar das raízes. Ele foi projetado para que o lugar das raízes passasse pelo ponto -3.859 + 2,82842j. O compensador é da forma (s+1)/(s+12.29645) com ganho de 536.
A função lsim do scipy.signal estava dando problema com os argumentos por isso preferi utilizar apenas as funções da biblioteca control.


Bibliografia

Digital Signal Processing - Monson H. Hayes
Engenharia de Controle Moderno - Katsuhiko Ogata
