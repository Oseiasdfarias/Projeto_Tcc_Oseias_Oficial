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

import matplotlib
import matplotlib.pyplot as plt
import scienceplots  # noqa: F401

plt.style.use('science')
# matplotlib.style.use("Solarize_Light2")
matplotlib.use('TkAgg')


class GraficosSinais(object):

    def __init__(self, markersize: float = 3.0, grid: bool = True):
        self.grid = grid
        self.markersize = markersize
        self.fig = plt.figure(figsize=(9.85, 6.45))
        self.config_axes()

        # fig.suptitle('Gráficos Sensor MPU6050', fontsize=19)
        self.fig.subplots_adjust(wspace=0.25, hspace=0.3, left=0.08,
                                 top=0.93, right=0.971, bottom=0.08)

    def get_fig_axes_ln(self):
        return self.fig, self.ax, self.ln

    def config_axes(self):
        self.ax1 = self.fig.add_subplot(221)
        self.ax1.set_title("Referência + Ângulo (Graus)",
                           color="#3B4252", fontsize=12)
        self.ax1.set_xlabel("Tempo")
        self.ax1.set_ylabel("Amplitude")
        self.ln_1, = self.ax1.plot([], [], marker=".",
                                   markersize=self.markersize,
                                   lw=1.2, label="Ref.", color="red")
        self.ln1, = self.ax1.plot([], [], lw=1.2, marker=".",
                                  markersize=self.markersize,
                                  label="Saída", color="sienna")
        self.ax1.grid(self.grid)
        plt.legend()

        self.ax2 = self.fig.add_subplot(222)
        self.ax2.set_title("Sinal de Erro (Graus)",
                           color="#3B4252", fontsize=12)
        self.ax2.set_xlabel("Tempo")
        self.ax2.set_ylabel("Amplitude")
        self.ln2, = self.ax2.plot([], [], lw=1.2, marker=".",
                                  markersize=self.markersize, color="green")
        self.ax2.grid(self.grid)

        self.ax3 = self.fig.add_subplot(223)
        self.ax3.set_title("Sinal de Controle (Volts)",
                           color="#3B4252", fontsize=12)
        self.ax3.set_xlabel("Tempo")
        self.ax3.set_ylabel("Amplitude")
        self.ln3, = self.ax3.plot([], [], lw=1.2, marker=".",
                                  markersize=self.markersize, color="purple")
        self.ax3.grid(self.grid)

        self.ax4 = self.fig.add_subplot(224)
        self.ax4.set_title("Sinal de Controle PWM (Volts RMS)",
                           color="#3B4252", fontsize=12)
        self.ax4.set_xlabel("Tempo")
        self.ax4.set_ylabel("Amplitude")
        self.ln4, = self.ax4.plot([], [], marker=".",
                                  markersize=self.markersize,
                                  lw=1.2, color="orange")
        self.ax4.grid(self.grid)

        # Axis que para plotar os gráficos
        self.ln = [self.ln_1, self.ln1, self.ln2, self.ln3, self.ln4]
        self.ax = [self.ax1, self.ax2, self.ax3, self.ax4]
