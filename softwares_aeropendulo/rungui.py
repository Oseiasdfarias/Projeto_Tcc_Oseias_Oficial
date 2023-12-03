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

import argparse

# Módulos da Interface Gráfica de Usuário
from src_interface import InterfaceAeropendulo
from src_interface.graficos_sinais import GraficosSinais

# Modulos do Gêmeo Digital
from simulador_aeropendulo.simulador import Simulador
from simulador_aeropendulo.graficos_aeropendulo import Graficos
from simulador_aeropendulo import AnimacaoAeropendulo


class RunInterface:

    def __init__(self) -> None:
        simular = self.get_args()
        self.runinterface(simular)

    def get_args(self) -> bool:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-simular", "--Output",
            help="""Para habilitar o simulador, use a sintax:
                    python rungui.py -simular sim""")
        args = parser.parse_args()
        if args.Output == "sim":
            return True
        else:
            return False

    def runinterface(self, simular):
        if simular:
            simulador = Simulador(Graficos(), AnimacaoAeropendulo())
        else:
            simulador = None
        InterfaceAeropendulo(GraficosSinais,
                             simulador, baud_rate=115200,
                             amostras=80.0, tela_fixa=True)


if __name__ == "__main__":
    RunInterface()
