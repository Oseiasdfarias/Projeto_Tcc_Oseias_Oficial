# ----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# ----------------------------------------------------
#
# Laboratório Virtual Sistemas Dinâmicos e Controle
# Tema: Simulação Aeropêndulo
# Autor: Oséias Farias
# Orientadores: Prof. Dr: Raphael Teixeira,
#               Prof. Dr: Rafael Bayma
#  ----------------------------------------------------

import vpython as vp
from graficos_aeropendulo import Graficos


class AnimacaoAeropendulo:
    """Classe que implementa a aminação do Aeropêndulo."""
    def __init__(self, comprimento_braco=4.4):
        # Parâmetros do Aeropêndulo
        self.comprimento_braco = comprimento_braco
        self.scene = vp.canvas(title="<center><h1>Aeropêndulo</h1><center/>",
                               width=650,
                               height=580, align="left", autoscale=0, range=5,
                               center=vp.vec(0, 3, 0),
                               background=vp.vector(1.7, 0.7, 0.9),
                               color=vp.vec(1, 0.6, 0.6),
                               forward=vp.vec(-0.3, 0, -1))
        # chamando a função para criar a aminação gráfica do Aeropêndulo.
        self.aeropendulo = self.aminacao()

    def aminacao(self):
        # Ambiente de sinulação.
        self.base = vp.box(pos=vp.vec(0, -0.85, 0), size=vp.vec(30, 0.2, 15),
                           texture=vp.textures.wood)
        self.parede = vp.box(pos=vp.vec(0, 7.1, -7.55),
                             size=vp.vec(30, 16, 0.2),
                             color=vp.vec(0.1, 0.1, 0.1), shininess=0.05)
        self.sitio = vp.text(pos=vp.vec(0, 8.1, -7.45),
                             text="AEROPÊNDULO", color=vp.vec(1, 0.6, 0.6),
                             align='center', depth=0)

        # Braço do Aeropêndulo.
        self.barra = vp.box(pos=vp.vec(0, -1.4, 0),
                            size=vp.vec(0.2, self.comprimento_braco, 0.2),
                            color=vp.vec(0.5, 0.5, 0.95))

        # Base que acopla o motor ao braço.
        self.base_motor = vp.cylinder(pos=vp.vec(-0.2, -4, 0), radius=0.4,
                                      axis=vp.vec(0.4, 0, 0),
                                      color=vp.vec(0.5, 0.5, 0.95))
        # Armadura do motor.
        self.base2_motor = vp.box(pos=vp.vec(0.4, -4, 0),
                                  size=vp.vec(0.4, 0.4, 0.4),
                                  color=vp.vec(1, 1, 0))

        # Eixo que da hélice do motor
        self.base_helice = vp.cylinder(pos=vp.vec(0.4, -4, 0), radius=0.05,
                                       axis=vp.vec(0.4, 0, 0),
                                       color=vp.vec(0.5, 0.5, 0.8))

        # Hélice.
        self.helice = vp.box(pos=vp.vec(0.8, -4, 0),
                             size=vp.vec(0.05, 0.2, 2),
                             color=vp.vec(1, 1, 0))

        # Motor completo.
        self.motor = vp.compound([self.base_motor,
                                  self.base2_motor,
                                  self.base_helice])

        # Motor + Hélice.
        self.motor_helice = vp.compound([self.motor, self.helice])

        # Aeropêndulo
        self.pendulo = self.barra# vp.compound([self.barra, self.motor_helice])
        self.pendulo.pos = vp.vec(0.31, 2.7, 0)

        # Eixo de sustentação.
        self.eixo = vp.cylinder(pos=vp.vec(0, 5.2, 0.3), radius=0.09,
                                axis=vp.vec(0, 0, -2),
                                color=vp.vec(0.7, 0.4, 0.1))

        # Estrutura de sustentação do aeropêndulo.
        self.b1 = vp.box(pos=vp.vec(0, 1.7, -2), size=vp.vec(3, 8, 0.6),
                         color=vp.vec(0.8, 0.8, 0.8))

        self.b2 = vp.box(pos=vp.vec(0, -0.6, -1.5), size=vp.vec(4.5, 0.4, 2.5),
                         color=vp.vec(0.8, 0.8, 0.8))

        self.logo = vp.box(pos=vp.vec(0, 2.5, -1.7),
                           texture="https://i.imgur.com/odcLHxB.png",
                           size=vp.vec(2, 2, 0.2))

        self.ufpa = vp.text(pos=vp.vec(0, 3.7, -1.7), text="UFPA",
                            color=vp.vec(1, 0.6, 0.6), height=0.5,
                            align='center', depth=0)

        return self.pendulo


if __name__ == "__main__":

    aeropendulo = AnimacaoAeropendulo()
    g = Graficos()
    graf, plot1, plot2 = g.graficos()
    aeropendulo.w = 10
    aeropendulo.angulo = 0
    aeropendulo.l = 3
    dt = 0.01
    t = 0

    while True:
        vp.rate(20)
        t += dt
        aeropendulo.a = -98*vp.sin(aeropendulo.angulo)/aeropendulo.l
        aeropendulo.w = aeropendulo.w + aeropendulo.a*dt
        aeropendulo.angulo = aeropendulo.angulo + aeropendulo.w*dt
        aeropendulo.aeropendulo.rotate(axis=vp.vec(0, 0, 1),
                                       angle=aeropendulo.w*dt,
                                       origin=vp.vec(0, 5.2, 0))
        aeropendulo.motor_helice.pos = aeropendulo.aeropendulo.pos
        aeropendulo.motor_helice.axis = aeropendulo.aeropendulo.axis
        aeropendulo.motor_helice.rotate(axis=vp.vec(1, 0, 0),
                                 angle=0.1)
        print(aeropendulo.helice.pos)
        plot1.plot(t, aeropendulo.a)
        plot2.plot(t, aeropendulo.w)
