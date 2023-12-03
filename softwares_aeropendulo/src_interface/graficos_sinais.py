# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para criar os gráficos da aplicação
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import scienceplots  # noqa: F401
from mplfonts import use_font
import numpy as np

from src_interface.interfaces.graficos_sinais import GraficosSinaisInterface

plt.style.use(['science', 'no-latex'])

use_font('Fira Code')

plt.rcParams.update({
    "font.size": 11,
    'text.color': "black",
    'axes.labelcolor': "black",
    'text.color': "black",
    'axes.labelcolor': "black",
    'axes.titlecolor': "#2B2B2B",
    'axes.titleweight': "bold"})

mpl.use('TkAgg')


class GraficosSinais(GraficosSinaisInterface):

    def __init__(self, markersize: float = 3.0,
                 grid: bool = True) -> None:
        self.grid = grid
        self.markersize = markersize
        self.fig = plt.figure(figsize=(9.85, 6.45), facecolor="#FFFFFF")
        self.config_axes()

        self.fig.subplots_adjust(wspace=0.2, hspace=0.45, left=0.08,
                                 top=0.93, right=0.971, bottom=0.12)

    def get_fig_axes_ln(self):
        return self.fig, self.ax, self.ln

    def config_axes(self) -> None:
        self.ax1 = self.fig.add_subplot(221)
        self.ax1.set_title("Referência + Ângulo (Graus)",
                           color="#2B2B2B", fontsize=9)
        self.ax1.set_xlabel("Tempo", color="#2B2B2B", fontsize=9)
        self.ax1.set_ylabel("Amplitude", color="#2B2B2B", fontsize=9)
        self.ln_1, = self.ax1.plot([], [], marker=".",
                                   markersize=self.markersize,
                                   lw=1.2, label="Ref.", color="red")
        self.ln1, = self.ax1.plot([], [], lw=1.2, marker=".",
                                  markersize=self.markersize,
                                  label="Saída", color="sienna")
        plt.yticks(np.arange(-50, 176, 25), rotation=45)
        plt.xticks(rotation=45)
        self.ax1.tick_params(axis='both', which='major', labelsize=9)
        self.ax1.tick_params(axis='both', which='minor', labelsize=7)

        plt.grid(which='major', color='#CCCCCC', linestyle='-', alpha=1)
        plt.grid(which='minor', color='#CCCCCC', linestyle=':', alpha=0.5)
        self.ax1.grid(self.grid)
        plt.legend()

        self.ax2 = self.fig.add_subplot(222)
        self.ax2.set_title("Sinal de Erro (Graus)",
                           color="#2B2B2B", fontsize=9)
        self.ax2.set_xlabel("Tempo", color="#2B2B2B", fontsize=9)
        self.ax2.set_ylabel("Amplitude", color="#2B2B2B", fontsize=9)
        self.ln2, = self.ax2.plot([], [], lw=1.2, marker=".",
                                  markersize=self.markersize, color="green")
        plt.yticks(np.arange(-60, 61, 15), rotation=45)
        plt.xticks(rotation=45)
        self.ax2.tick_params(axis='both', which='major', labelsize=9)
        self.ax2.tick_params(axis='both', which='minor', labelsize=7)

        plt.grid(which='major', color='#CCCCCC', linestyle='-', alpha=1)
        plt.grid(which='minor', color='#CCCCCC', linestyle=':', alpha=0.5)
        self.ax2.grid(self.grid)

        self.ax3 = self.fig.add_subplot(223)
        self.ax3.set_title("Sinal de Controle (Volts)",
                           color="#2B2B2B", fontsize=9)
        self.ax3.set_xlabel("Tempo", color="#2B2B2B", fontsize=9)
        self.ax3.set_ylabel("Amplitude", color="#2B2B2B", fontsize=9)
        self.ln3, = self.ax3.plot([], [], lw=1.2, marker=".",
                                  markersize=self.markersize, color="purple")
        plt.yticks(np.arange(-1, 2, 0.5), rotation=45)
        plt.xticks(rotation=45)
        self.ax3.tick_params(axis='both', which='major', labelsize=9)
        self.ax3.tick_params(axis='both', which='minor', labelsize=7)

        plt.grid(which='major', color='#CCCCCC', linestyle='-', alpha=1)
        plt.grid(which='minor', color='#CCCCCC', linestyle=':', alpha=0.5)
        self.ax3.grid(self.grid)

        self.ax4 = self.fig.add_subplot(224)
        self.ax4.set_title("Sinal Entrada Malha Aberta (Volts RMS)",
                           color="#2B2B2B", fontsize=9)
        self.ax4.set_xlabel("Tempo", color="#2B2B2B", fontsize=9)
        self.ax4.set_ylabel("Amplitude", color="#2B2B2B", fontsize=9)
        self.ln4, = self.ax4.plot([], [], marker=".",
                                  markersize=self.markersize,
                                  lw=1.2, color="orange")
        plt.yticks(np.arange(0, 3.5, 0.5), rotation=45)
        plt.xticks(rotation=45)
        self.ax4.tick_params(axis='both', which='major', labelsize=9)
        self.ax4.tick_params(axis='both', which='minor', labelsize=7)

        plt.grid(which='major', color='#CCCCCC', linestyle='-', alpha=1)
        plt.grid(which='minor', color='#CCCCCC', linestyle=':', alpha=0.5)
        self.ax4.grid(self.grid)

        # Axis que para plotar os gráficos
        self.ln = [self.ln_1, self.ln1, self.ln2, self.ln3, self.ln4]
        self.ax = [self.ax1, self.ax2, self.ax3, self.ax4]
