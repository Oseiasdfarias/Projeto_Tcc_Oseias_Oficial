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

import numpy as np
from matplotlib.animation import FuncAnimation
from time import sleep
import os

import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Módulos criados
from src_interface import ColetaDados
from src_interface.lista_portas_usb import ListaPortasUsb

from src_interface.interfaces.graficos_sinais import GraficosSinaisInterface

from simulador_aeropendulo.interfaces.simulador import SimuladorInterface


class InterfaceAeropendulo:
    """Classe que constroi o FrontEnd do App Aeropendulo."""
    def __init__(self, graficos_sinais: GraficosSinaisInterface,
                 simulador: SimuladorInterface, baud_rate: int = 115200,
                 amostras: int = 50, Ts: float = 0.02,
                 tela_fixa: bool = False):
        self.tela_fixa = tela_fixa

        # Objeto para coletar dados do sensor
        self.usb_port = ""
        self.baud_rate = baud_rate

        self.amostras = amostras
        self.Ts = Ts

        self.simulador = simulador
        # Graficos
        self.executar = True
        self.graficos_sinais = graficos_sinais()
        self.fig, self.ax, self.ln = self.graficos_sinais.get_fig_axes_ln()

        # Inicializa a interface gráfica
        self.start_gui()

    def quit(self) -> None:
        self.root.quit()
        self.root.destroy()
        if os.name == "nt":
            _ = os.system("cls")
        # para mac e linux(aqui, os.name é 'posix')
        else:
            _ = os.system("clear")

    def set_usb_port(self, porta_atual: str) -> None:
        self.usb_port = porta_atual

    @staticmethod
    def aparencia_event(new_appearance_mode: str) -> None:
        ctk.set_appearance_mode(new_appearance_mode)

    def init(self) -> None:
        for i in range(4):
            if i == 0:
                self.ax[i].set_xlim(0, self.amostras*self.Ts)
                self.ax[i].set_ylim(-60, 180)
            elif i == 1:
                self.ax[i].set_xlim(0, self.amostras*self.Ts)
                self.ax[i].set_ylim(-60, 60)
            elif i == 2:
                self.ax[i].set_xlim(0, self.amostras*self.Ts)
                self.ax[i].set_ylim(-0.1, 4)
            elif i == 3:
                self.ax[i].set_xlim(0, self.amostras*self.Ts)
                self.ax[i].set_ylim(-0.1, 3)
            else:
                self.ax[i].set_xlim(0, self.amostras*self.Ts)
                self.ax[i].set_ylim(-60, 60)

            self.ax[i].axhline(0.0, color="black", lw=1.2)
            self.ax[i].axvline(0.01, color="black", lw=1.2)
        return self.ln

    def update(self, frame):
        dados = self.coleta_dados.get_dados()
        t = np.arange(0, 0.02*len(dados[0]), 0.02)
        for i, ax in enumerate(self.ln):
            ax.set_xdata(t)
            ax.set_ydata(dados[i])
        return self.ln

    def run_graph(self) -> None:
        if self.executar:
            if self.usb_port:
                self.coleta_dados = ColetaDados(
                    self.amostras, porta=self.usb_port,
                    baud_rate=self.baud_rate)
                sleep(0.5)
                self.coleta_dados.set_sinal("12000")
                self.ani = FuncAnimation(self.fig, self.update,
                                         init_func=self.init,
                                         cache_frame_data=False,
                                         interval=20, blit=True)
                sleep(0.5)
                self.executar = False

    def switch_event_den_serra(self) -> None:
        if self.switch_var_den_serra.get() == "on":
            self.switch_quad.deselect(0)
            self.switch_seno.deselect(0)
            if not self.executar:
                self.coleta_dados.set_sinal("7000")
        else:
            self.switch_den_serra.select(1)

    def switch_event_seno(self) -> None:
        if self.switch_var_seno.get() == "on":
            self.switch_den_serra.deselect(0)
            self.switch_quad.deselect(0)
            if not self.executar:
                self.coleta_dados.set_sinal("8000")
        else:
            self.switch_seno.select(1)

    def switch_event_quad(self) -> None:
        if self.switch_var_quad.get() == "on":
            self.switch_den_serra.deselect(0)
            self.switch_seno.deselect(0)
            if not self.executar:
                self.coleta_dados.set_sinal("9000")
        else:
            self.switch_quad.select(1)

    def switch_event_mamb(self) -> None:
        if not self.executar:
            if self.switch_var_mamf.get() == "on":
                if not self.executar:
                    self.coleta_dados.set_sinal("10000")
            else:
                if not self.executar:
                    self.coleta_dados.set_sinal("11000")
        else:
            self.switch_mamf.deselect(0)
            return

    def switch_event_sdados(self) -> None:
        if self.executar:
            self.switch_salve.deselect(0)
            return

        if self.switch_var_sdados.get() == "on":
            self.coleta_dados.flag_salvar_dados = True
        else:
            self.coleta_dados.flag_salvar_dados = False
            self.coleta_dados.salvar_dados_colhidos()
            self.salvar_dados = np.array([[], [], [],
                                          [], [], [], []]).astype(object)

    def get_data_emtry_ampl1(self) -> None:
        data = self.emtry_ampl1.get()
        isnum = data.replace('.', '', 1).isdigit()
        if not self.executar and isnum:
            if (0 <= float(data) <= 30):
                self.ampl_label1.configure(
                    text=f"{data}°")
                self.coleta_dados.set_amplitude(data)
        self.emtry_ampl1.delete(0, len(data))

    def get_data_emtry_freq1(self) -> None:
        data = self.emtry_freq1.get()
        print(f"Dado entrada freq 1: {data.isdigit()}")
        isnum = data.replace('.', '', 1).isdigit()
        if not self.executar and isnum:
            if (0.0 <= float(data) <= 5.0):
                self.freq_label1.configure(
                    text=f"{data} rad/s")
                self.coleta_dados.set_frequencia(data)
        self.emtry_freq1.delete(0, len(data))

    def get_data_emtry_offset1(self) -> None:
        data = self.emtry_offset1.get()
        isnum = data.replace('.', '', 1).isdigit()
        if not self.executar and isnum:
            if (0 <= float(data) <= 120.):
                self.offset_label1.configure(
                    text=f"{data}°")
                self.coleta_dados.set_offset(data)
        self.emtry_offset1.delete(0, len(data))

    def start_gui(self) -> None:
        """
            Componentes da interface GUI.
        """
        ctk.set_default_color_theme("green")
        self.root = ctk.CTk()
        ctk.set_appearance_mode("Dark")
        self.root.title("Interface Aeropêndulo")
        self.root.geometry("1270x700+40+5")
        if self.tela_fixa:
            self.root.minsize(1270, 700)
            self.root.maxsize(1270, 700)
        self.root.state("normal")

        # =====================================================================
        # +++++++++++++++++++ Frame para adicionar os Menus +++++++++++++++++++
        # =====================================================================
        self.frame_menus = ctk.CTkFrame(master=self.root, width=5, height=5)
        self.frame_menus.grid(row=0, column=0, padx=10, pady=5, sticky="sn")

        self.frame_menu = ctk.CTkFrame(master=self.frame_menus,
                                       width=5, height=5)
        self.frame_menu.grid(row=2, column=0, padx=10, pady=5, sticky="s")

        self.frame_dados = ctk.CTkFrame(master=self.frame_menus,
                                        width=5, height=10)
        self.frame_dados.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.frame_controle = ctk.CTkFrame(master=self.frame_menus,
                                           width=5, height=10)
        self.frame_controle.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # +++++++++++++++++ Frame para adicionar os gráficos ++++++++++++++++++
        self.frame_graficos = ctk.CTkFrame(master=self.root,
                                           width=5, height=5)
        self.frame_graficos.grid(row=0, column=1, padx=0, pady=5, sticky="sn")

        self.label = ctk.CTkLabel(
            self.frame_graficos, text="Interface Aeropêndulo",
            font=ctk.CTkFont(
                size=20, weight="bold")).grid(column=1, row=0)

        # ===================================================================
        # ++++++++++++++++++++++ Widgets Frame de Menu ++++++++++++++++++++++
        # ===================================================================
        _ = ctk.CTkLabel(master=self.frame_menu, text=" ", width=230)
        _.grid(row=7, column=0, padx=0, pady=0)
        self.label_nemu = ctk.CTkLabel(master=self.frame_menu, text="Menu",
                                       # image=self.logo_image,
                                       width=50,
                                       font=ctk.CTkFont(size=20,
                                                        weight="bold"))
        self.label_nemu.grid(row=0, column=0, padx=10, pady=4, sticky="w")

        canvas = FigureCanvasTkAgg(self.fig, master=self.frame_graficos)
        canvas.get_tk_widget().grid(column=1, row=1,
                                    padx=5, pady=4, sticky="sn")

        button_run = ctk.CTkButton(master=self.frame_menu, height=30,
                                   font=ctk.CTkFont(size=15, weight="bold"),
                                   text="Executar", border_width=1,
                                   command=self.run_graph)
        button_run.grid(row=2, column=0, padx=10, pady=4, sticky="w")

        self.switch_var_mamf = ctk.StringVar(value="off")
        self.switch_mamf = ctk.CTkSwitch(master=self.frame_menu,
                                         text="MA/MF",
                                         width=40,
                                         switch_height=25,
                                         switch_width=40,
                                         progress_color=("#2CC985", "orange"),
                                         command=self.switch_event_mamb,
                                         font=ctk.CTkFont(size=15,
                                                          weight="normal"),
                                         variable=self.switch_var_mamf,
                                         onvalue="on", offvalue="off")

        self.switch_mamf.grid(row=3, column=0, padx=10, pady=4, sticky="w")

        self.switch_var_sdados = ctk.StringVar(value="off")
        self.switch_salve = ctk.CTkSwitch(master=self.frame_menu,
                                          text="Salvar Dados",
                                          width=40,
                                          switch_height=25,
                                          switch_width=40,
                                          progress_color=("#2CC985", "orange"),
                                          command=self.switch_event_sdados,
                                          font=ctk.CTkFont(size=15,
                                                           weight="normal"),
                                          variable=self.switch_var_sdados,
                                          onvalue="on", offvalue="off")

        self.switch_salve.grid(row=4, column=0, padx=10, pady=4, sticky="w")

        self.usb_menu = ctk.CTkOptionMenu(
                            master=self.frame_menu,
                            height=25,
                            font=ctk.CTkFont(
                                size=15,
                                weight="bold"),
                            values=["None"],
                            command=self.set_usb_port)
        self.usb_menu.grid(row=5, column=0, padx=10, pady=4, sticky="w")

        self.aparencia_menu = ctk.CTkOptionMenu(master=self.frame_menu,
                                                height=25,
                                                font=ctk.CTkFont(
                                                     size=15,
                                                     weight="bold"),
                                                values=["Dark", "Light"],
                                                command=self.aparencia_event)

        self.aparencia_menu.grid(row=6, column=0, padx=10, pady=4, sticky="w")

        button = ctk.CTkButton(master=self.frame_menu, height=30,
                               font=ctk.CTkFont(size=15, weight="bold"),
                               text="Quit", border_width=1,
                               fg_color=("red", "red"),
                               text_color=("white", "white"),
                               hover_color=("#C11C1C", "#C11C1C"),
                               command=self.quit)
        button.grid(row=7, column=0,
                    padx=10, pady=10, sticky="w")

        # ================================================================
        # +++++++++++++++++ Widgets Frame de Sinais ++++++++++++++++++++++
        # ================================================================
        self.label_sinais = ctk.CTkLabel(
            master=self.frame_dados,
            text="Informações",
            width=150,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.label_sinais.grid(row=0, column=0, padx=5, pady=3, sticky="s")

        self.ampl_label = ctk.CTkLabel(
            master=self.frame_dados,
            text="Amplitude: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.ampl_label.grid(row=1, column=0, padx=0, pady=4)

        self.ampl_label1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="20.0°",
            width=70,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.ampl_label1.grid(row=1, column=1, padx=0, pady=0)

        self.freq_label = ctk.CTkLabel(
            master=self.frame_dados,
            text="Frequência: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.freq_label.grid(row=2, column=0, padx=0, pady=4)

        self.freq_label1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="1.0 rad/s",
            width=60,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.freq_label1.grid(row=2, column=1, padx=0, pady=0)

        self.offset_label = ctk.CTkLabel(
            master=self.frame_dados,
            text="Offset: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.offset_label.grid(row=3, column=0, padx=0, pady=4)

        self.offset_label1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="60.0°",
            width=60,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.offset_label1.grid(row=3, column=1, padx=0, pady=0)

        self.label_erro = ctk.CTkLabel(
            master=self.frame_dados,
            text="Sinal de Erro: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.label_erro.grid(row=4, column=0, padx=0, pady=4)

        self.label_erro1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="15°",
            width=50,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.label_erro1.grid(row=4, column=1, padx=0, pady=2)

        # ===================================================================
        # ++++++++++++++++++++ Widgets Frame de Sinais ++++++++++++++++++++++
        # ===================================================================
        self.label_nemu1 = ctk.CTkLabel(master=self.frame_controle,
                                        text="Sinal de ref.",
                                        width=120,
                                        font=ctk.CTkFont(size=20,
                                                         weight="bold"))
        self.label_nemu1.grid(row=0, column=0, padx=5, pady=4)

        self.btn_ampl = ctk.CTkButton(master=self.frame_controle, width=130,
                                      height=30, font=ctk.CTkFont(
                                                    size=15, weight="bold"),
                                      fg_color=("red", "purple"),
                                      text_color=("white", "white"),
                                      hover_color=("#C11C1C", "#4A0255"),
                                      text="Add Amplitude:", border_width=1,
                                      command=self.get_data_emtry_ampl1)
        self.btn_ampl.grid(row=1, column=0, padx=5, pady=4, sticky="w")

        self.emtry_ampl1 = ctk.CTkEntry(master=self.frame_controle,
                                        width=85,
                                        font=ctk.CTkFont(size=17,
                                                         weight="bold"),
                                        placeholder_text="[0 à 30]")
        self.emtry_ampl1.grid(row=1, column=1,
                              padx=(0, 5), pady=4, sticky="s")

        self.btn_freq = ctk.CTkButton(master=self.frame_controle, width=130,
                                      height=30, font=ctk.CTkFont(
                                                    size=15, weight="bold"),
                                      fg_color=("red", "purple"),
                                      text_color=("white", "white"),
                                      hover_color=("#C11C1C", "#4A0255"),
                                      text="Add Frequência:", border_width=1,
                                      command=self.get_data_emtry_freq1)
        self.btn_freq.grid(row=2, column=0, padx=5, pady=4, sticky="w")

        self.emtry_freq1 = ctk.CTkEntry(master=self.frame_controle,
                                        width=85,
                                        font=ctk.CTkFont(size=17,
                                                         weight="bold"),
                                        placeholder_text="[0 à 5]")
        self.emtry_freq1.grid(row=2, column=1,
                              padx=(0, 5), pady=4, sticky="s")

        self.btn_offset = ctk.CTkButton(
            master=self.frame_controle, width=130,
            height=30, font=ctk.CTkFont(
                size=15, weight="bold"),
            fg_color=("red", "purple"),
            text_color=("white", "white"),
            hover_color=("#C11C1C", "#4A0255"),
            text="Add Offset:", border_width=1,
            command=self.get_data_emtry_offset1)
        self.btn_offset.grid(row=3, column=0, padx=5, pady=4, sticky="w")

        self.emtry_offset1 = ctk.CTkEntry(
            master=self.frame_controle,
            width=85, font=ctk.CTkFont(size=17,
                                       weight="bold"),
            placeholder_text="[0 à 120]")
        self.emtry_offset1.grid(row=3, column=1,
                                padx=(0, 5), pady=4, sticky="s")

        self.switch_var_den_serra = ctk.StringVar(value="off")
        self.switch_den_serra = ctk.CTkSwitch(
            master=self.frame_controle,
            text="Dente Serra",
            width=40,
            switch_height=25,
            switch_width=40,
            progress_color=("#2CC985", "orange"),
            command=self.switch_event_den_serra,
            font=ctk.CTkFont(size=15,
                             weight="normal"),
            variable=self.switch_var_den_serra,
            onvalue="on", offvalue="off")
        self.switch_den_serra.grid(row=4, column=0, padx=5, pady=4, sticky="w")

        self.switch_var_quad = ctk.StringVar(value="on")
        self.switch_quad = ctk.CTkSwitch(
            master=self.frame_controle,
            text="Quadrada",
            width=40,
            switch_height=25,
            switch_width=40,
            progress_color=("#2CC985", "orange"),
            command=self.switch_event_quad,
            font=ctk.CTkFont(size=15,
                             weight="normal"),
            variable=self.switch_var_quad,
            onvalue="on", offvalue="off")
        self.switch_quad.grid(row=5, column=0, padx=5, pady=4, sticky="w")

        self.switch_var_seno = ctk.StringVar(value="off")
        self.switch_seno = ctk.CTkSwitch(
            master=self.frame_controle,
            text="Senoidal",
            width=40,
            switch_height=25,
            switch_width=40,
            progress_color=("#2CC985", "orange"),
            command=self.switch_event_seno,
            font=ctk.CTkFont(size=15,
                             weight="normal"),
            variable=self.switch_var_seno,
            onvalue="on", offvalue="off")
        self.switch_seno.grid(row=6, column=0, padx=5, pady=4, sticky="w")

        self.lista_usb = ListaPortasUsb(self.usb_menu, self.set_usb_port)
        self.root.mainloop()  # Loop infinito da interface
        # for windows
        if os.name == "nt":
            _ = os.system("cls")
        # para mac e linux(aqui, os.name é 'posix')
        else:
            _ = os.system("clear")
