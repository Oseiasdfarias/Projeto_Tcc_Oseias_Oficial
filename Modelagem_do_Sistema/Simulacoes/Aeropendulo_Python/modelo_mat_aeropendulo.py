import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.style.use("ggplot")


class ModeloAeropendulo:
    def __init__(self, K_m=0.0296, m=0.36, d=0.03,
                 J=0.0106, g=9.8, c=0.0076):
        # Parâmetros do Aeropêndulo.
        self.K_m = K_m
        self.m = m
        self.d = d
        self.J = J
        self.g = g
        self.c = c

        # Configuração para simulação
        self.t_simu = 0
        self.ts = 0
        self.t = 0
        self.x = 0

    # Define o nome da função que modela o sistema;
    def modelo_aeropendulo(self, x, t):
        x1, x2 = x        # Variáveis de estado a partir do vetor de estados;
        dx1 = x2          # Função de estado dx1 = f(x,u)

        # Função de estado dx2 = f(x,u)
        dx2 = -(self.m*self.g*self.d / self.J) * x1 - (self.c / self.J) * x2 + (self.K_m / self.J) * 0
        dx = np.array([dx1, dx2])      # Derivada do vetor de estados
        return dx                      # Retorna a derivada do vetor de estados

    def simular(self, t_simu=100, ts=0.1, x_0=[0.1, -0.5]):
        self.t_simu = t_simu
        self.ts = ts
        self.t = ts*np.arange(0, t_simu+ts, ts)

        # Condições iniciais
        x_0 = x_0

        # Integração com método odeint() da biblioteca scipy.integrate
        self.x = odeint(self.modelo_aeropendulo, x_0, self.t)
        return self.x

    def plotar_graficos(self):
        plt.figure(figsize=(10, 7))
        plt.suptitle("Gráficos dos estados do Aeropêndulo")

        plt.subplot(211)
        plt.plot(self.t, self.x[:, 0])

        plt.subplot(212)
        plt.plot(self.t, self.x[:, 1])
        plt.show()


if __name__ == "__main__":
    aeropendulo_1 = ModeloAeropendulo()
    aeropendulo_1.simular()
    aeropendulo_1.plotar_graficos()
