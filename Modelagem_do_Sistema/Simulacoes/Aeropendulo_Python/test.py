from modelo_mat_aeropendulo import ModeloMatAeropendulo
import numpy as np
import matplotlib.pyplot as plt


MMA = ModeloMatAeropendulo()
MMA.simular(t_simu=1e3, ts=1e-2)
MMA.simulacao_dinamica(t_simu=1e3, ts=1e-2)

x1 = [[], []]
t_simu = 1e3
ts = 1e-2
# Condições Iniciais dos estados
x = [0.1, -0.5]
t = 0
t1 = []
ant = 0
for i in range(1000):
    dx = MMA.modelo_aeropendulo(x, t)
    dt = t - ant
    x = x + dt * dx
    x1[0].append(x[0])
    x1[1].append(x[1])

    t1.append(t)
    ant = t
    t += ts

print("x1[0]", len(x1[0]))
print("t", len(t1))
plt.figure("fig1", figsize=(10, 7))
plt.suptitle("Gráficos Dinâmico dos estados do Aeropêndulo")
plt.subplot(111)
plt.plot(t1, x1[0])
plt.plot(t1, x1[1])

MMA.plotar_graficos()
