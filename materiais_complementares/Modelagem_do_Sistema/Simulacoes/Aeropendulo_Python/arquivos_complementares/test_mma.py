import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 1.0  # Massa;
b = 0.8  # Coeficiente de amortecimento;
k = 1.2  # Constante elástica da mola;

def MMA(x, t):                           # Define o nome da função que modela o sistema;
  x1, x2 = x                            # Variáveis de estado a partir do vetor de estados;
  dx1 = x2                              # Função de estado dx1 = f(x,u)
  dx2 = -(k/m)*x1 - (b/m)*x2 +(1/m)*0   # Função de estado dx2 = f(x,u)
  dx = np.array([dx1, dx2])               # Derivada do vetor de estados
  return dx

T = 100                       # Tempo total de simulação
Ts = 0.1                      # Período de amostragem (passo de integração)
t = Ts*np.arange(0, T+Ts, Ts)
x0 = [0.1, -0.5]

# Integração numérica: odeint integra a função MMA 
# com condição inicial x0 durante o tempo t.
x = odeint(MMA, x0, t)
f1 = plt.figure(figsize = (10,4))
plt.subplot(211)
plt.plot(t,x[:,0])
plt.grid()
plt.subplot(212)
plt.plot(t,x[:,1])
plt.grid()

# Integração numérica: odeint integra a função MMA 
# com condição inicial x0 durante o tempo t.
x1 = [[], []]
for j, i in enumerate(t):
    dx = MMA(x0, Ts)
    try:
        x0 = x0+dx*(t[j+1]-t[j])
    except:
        pass
    x1[0].append(x0[0])
    x1[1].append(x0[1])

f2 = plt.figure(figsize = (10,4))
plt.subplot(211)
plt.plot(t, x1[0])
plt.grid()
plt.subplot(212)
plt.plot(t, x1[1])
plt.grid()
plt.show()
