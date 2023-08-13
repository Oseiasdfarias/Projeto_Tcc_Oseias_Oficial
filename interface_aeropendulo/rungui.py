# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para criar a Interface Gráfica do Aeropêndulo
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

from src_interface import InterfaceAeropendulo
from src_interface.graficos_sinais import GraficosSinais


def runinterface():
    InterfaceAeropendulo(GraficosSinais, baud_rate=115200,
                         amostras=80.0, tela_fixa=True)


if __name__ == "__main__":
    runinterface()
