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
from simulador_aeropendulo import (Graficos, AnimacaoAeropendulo)

from .interfaces.graficos_aeropendulo import GraficosInterface
from .interfaces.animacao_aeropendulo import AnimacaoAeropenduloInterface
from .interfaces.simulador import SimuladorInterface


class Simulador(SimuladorInterface):

    def __init__(self, graficos: GraficosInterface,
                 animacao_aeropendulo: AnimacaoAeropenduloInterface) -> None:
        self.t = 0
        self.t_ant = 0
        self.ts = 0
        self.theta_rad = 0
        self.theta_rad_ant = 0
        self.dtheta_rad = 0
        # Instanciando um objeto AeropenduloAaeropendulo()
        self.animacao_aeropendulo = animacao_aeropendulo

        # Instanciando um objeto para plotagem dos gráficos dinâmicos dos
        # estados do Aeropêndulo
        self.g = graficos
        self.graf, self.plot1, self.plot2 = self.g.graficos()  # noqa

    def grau2rad(self, graus):
        return (graus)*(vp.pi/180.0)

    def rotate(self, angle) -> None:
        self.valor_angle = self.grau2rad(angle)
        self.animacao_aeropendulo.aeropendulo.rotate(axis=vp.vec(0, 0, 1),
                                                     angle=self.valor_angle,
                                                     origin=vp.vec(0, 5.2, 0))
        self.animacao_aeropendulo.set_posicao_helice(self.valor_angle)

    def atualizar_estados(self, t, theta, ref):
        self.t = t
        self.ts = self.t - self.t_ant
        self.theta_rad = self.grau2rad(theta)
        try:
            self.dtheta_rad = (self.theta_rad - self.theta_rad_ant)/self.ts
        except Exception as exception:
            print(exception)

        # Atualiza o ângulo do Aeropêndulo
        self.animacao_aeropendulo.aeropendulo.rotate(
                        axis=vp.vec(0, 0, 1),
                        angle=self.dtheta_rad*self.ts,
                        origin=vp.vec(0, 5.2, 0))

        # Animação da dinâmica da Hélice
        self.animacao_aeropendulo.update_helice(self.dtheta_rad, self.ts)

        # print(x[1] + interface.valor_angle)
        # Gráfico do ângulo.
        self.plot1.plot(t, theta)
        # Gráfico do sinal de referência
        self.plot2.plot(t, ref)
        # Gráfico da velocidade ângular.
        # self.plot3.plot(t, x[0])
        # Gráfico do sinal de controle
        # self.plot4.plot(t, u)
        self.t_ant = t
        self.theta_rad_ant = self.theta_rad


if __name__ == "__main__":
    simulador = Simulador(Graficos(), AnimacaoAeropendulo())
    # simulador.rotate(45)
    simulador.atualizar_estados(1, 2, 3)
