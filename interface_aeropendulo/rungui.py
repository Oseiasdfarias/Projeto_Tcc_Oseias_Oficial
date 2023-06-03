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

from interface import InterfaceAeropendulo


def runinterface():
    InterfaceAeropendulo(baud_rate=115200,
                         amostras=100.0, tela_fixa=True)


if __name__ == "__main__":
    runinterface()
