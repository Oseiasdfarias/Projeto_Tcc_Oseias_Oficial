# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# -----------------------------------------------------
#
# Laboratório Virtual Sistemas Dinâmicos e Controle
# Tema: Simulação Aeropêndulo
# Autor: Oséias Farias
# Orientadores: Prof. Dr: Raphael Teixeira,
#               Prof. Dr: Rafael Bayma
#
# Data: 2023
#  ----------------------------------------------------
#

import vpython as vp
# import numpy as np
from simulador_aeropendulo import (
    Graficos,
    AnimacaoAeropendulo
)
from interfaces.graficos_aeropendulo import GraficosInterface
from interfaces.animacao_aeropendulo import AnimacaoAeropenduloInterface


class Simulador:

    def __init__(self, graficos: GraficosInterface,
                 animacao_aeropendulo: AnimacaoAeropenduloInterface) -> None:
        self.t = 0
        self.t_ant = 0
        self.ts = 0
        self.x = [0, 0]
        # Instanciando um objeto AeropenduloAaeropendulo()
        self.animacao_aeropendulo = animacao_aeropendulo

        # Instanciando um objeto para plotagem dos gráficos dinâmicos dos
        # estados do Aeropêndulo
        self.g = graficos
        self.graf, self.plot1, self.plot2, self.plot3, self.plot4 = self.g.graficos()  # noqa

    def atualizar_estados(self, estados):
        # print(x[1]*(180/np.pi))
        self.t_ant = estados[0]
        self.t += self.ts
        self.x[0] = estados[1]
        # Atualiza o ângulo do Aeropêndulo
        self.animacao_aeropendulo.aeropendulo.rotate(
            axis=vp.vec(0, 0, 1),
            angle=self.x[0]*self.ts,
            origin=vp.vec(0, 5.2, 0))

        # Animação da dinâmica da Hélice
        self.animacao_aeropendulo.update_helice(self.x[0], self.ts)

        # print(x[1] + interface.valor_angle)
        # Gráfico do ângulo.
        # self.plot1.plot(t, x[1] + interface.valor_angle)
        # Gráfico do sinal de referência
        # self.plot2.plot(t, controlador.r + interface.valor_angle)
        # Gráfico da velocidade ângular.
        # self.plot3.plot(t, x[0])
        # Gráfico do sinal de controle
        # self.plot4.plot(t, u)


if __name__ == "__main__":
    simulador = Simulador(Graficos(), AnimacaoAeropendulo())
    simulador.atualizar_estados([1, 2, 3])
