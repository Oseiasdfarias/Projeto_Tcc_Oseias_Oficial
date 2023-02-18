
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# ----------------------------------------------------
# Laboratório Virtual Sistemas Dinâmicos e Controle
# Tema: Simulação Aeropêndulo
# Autor: Oséias Farias
# Orientadores: Prof. Dr: Raphael Teixeira,
#               Prof. Dr: Rafael Bayma
# ----------------------------------------------------
import vpython as vp
from graficos_aeropendulo import Graficos
from animacao_aeropendulo import AnimacaoAeropendulo
from modelo_mat_aeropendulo import ModeloMatAeropendulo

# Instanciando um objeto AeropenduloAaeropendulo = Aeropendulo()
animacao_aeropendulo = AnimacaoAeropendulo()

# Instanciando um objeto para plotagem dos gráficos dinâmicos dos
# estados do Aeropêndulo
g = Graficos()
graf, plot1, plot2, plot3 = g.graficos()

# Instânciando um objeto para solução matemática do sistema Aeropêndulo.
mod_mat_aeropendulo = ModeloMatAeropendulo()
mod_mat_aeropendulo.simulacao_dinamica(t_simu=1e3, ts=1e-2)
mod_mat_aeropendulo.plotar_graficos()

animacao_aeropendulo.w = 10
animacao_aeropendulo.angulo = 0
animacao_aeropendulo.l = 3
dt = 0.01
t = 0

while True:
    vp.rate(20)
    t += dt
    animacao_aeropendulo.a = -98*vp.sin(animacao_aeropendulo.angulo) / animacao_aeropendulo.l
    animacao_aeropendulo.w = animacao_aeropendulo.w + animacao_aeropendulo.a*dt
    animacao_aeropendulo.angulo = animacao_aeropendulo.angulo + animacao_aeropendulo.w*dt
    animacao_aeropendulo.aeropendulo.rotate(axis=vp.vec(0, 0, 1),
                                            angle=animacao_aeropendulo.w*dt,
                                            origin=vp.vec(0, 5.2, 0))
    plot1.plot(t, animacao_aeropendulo.a)
    plot2.plot(t, animacao_aeropendulo.w)
    plot3.plot(t, animacao_aeropendulo.angulo)
