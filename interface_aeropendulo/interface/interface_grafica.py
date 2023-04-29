import numpy as np
from matplotlib.animation import FuncAnimation
# import os
# from PIL import Image

# import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Modulos criados
from interface import (ColetaDados, GraficosSinais)
from interface.lista_portas_usb import ListaPortasUsb


class InterfaceAeropendulo:
    def __init__(self, tela_fixa=False):
        self.tela_fixa = tela_fixa
        # Objeto para coletar dados do sensor
        self.usb_port = None
        self.baud_rate = 115200

        # Graficos
        self.executar = True
        graficos_sinais = GraficosSinais()
        self.fig, self.ax, self.ln = graficos_sinais.get_fig_axes_ln()

        # tx = []

        # Inicializa a interface gráfica
        self.start_gui()

    def quit(self):
        self.root.quit()
        self.root.destroy()

    def set_usb_port(self, porta_atual):
        self.usb_port = porta_atual

    @staticmethod
    def aparencia_event(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def init(self):
        for i in range(4):
            """tx.append(ax[i].text(40, int(fila[i][-1])+2, f"{fila[i][-1]}",
                                color=[0.3, 0.3, 0.5],
                                fontsize=9,
                                fontweight="bold"))"""
            if i < 1:
                self.ax[i].set_xlim(0, 50)
                self.ax[i].set_ylim(-5, 180)
            if i >= 1:
                self.ax[i].set_xlim(0, 50)
                self.ax[i].set_ylim(-15, 15)
            self.ax[i].axhline(0, color="black", lw=1.2)
            self.ax[i].axvline(0.5, color="black", lw=1.2)
        return self.ln

    def update(self, frame):
        dados = self.coleta_dados.get_dados()
        t = np.arange(0, len(dados[0]))
        for i, ax in enumerate(self.ln):
            """tx[i].set_y(int(dados[i][-1]+2))
            if (i <= 2):
                tx[i].set_text(f"{dados[i][-1]:.2f}\nm/s^2")
            else:
                tx[i].set_text(f"{dados[i][-1]:.2f}\nrad/s")
            """
            ax.set_xdata(t)
            ax.set_ydata(dados[i])
        return self.ln

    def run_graph(self):
        if self.executar:
            if self.usb_port:
                self.coleta_dados = ColetaDados(porta=self.usb_port,
                                                baud_rate=self.baud_rate)
                self.ani = FuncAnimation(self.fig, self.update,
                                         init_func=self.init,
                                         cache_frame_data=False,
                                         interval=20, blit=True)
                self.executar = False

    def switch_event_deg(self):
        if self.switch_var_deg.get() == "on":
            self.switch_quad.deselect(0)
            self.switch_seno.deselect(0)
            if not self.executar:
                self.coleta_dados.set_sinal(f"deg:{1.0}")
        else:
            self.switch_deg.select(1)

    def switch_event_seno(self):
        if self.switch_var_seno.get() == "on":
            self.switch_deg.deselect(0)
            self.switch_quad.deselect(0)
            if not self.executar:
                self.coleta_dados.set_sinal(f"seno:{2.0}")
        else:
            self.switch_seno.select(1)

    def switch_event_quad(self):
        if self.switch_var_quad.get() == "on":
            self.switch_deg.deselect(0)
            self.switch_seno.deselect(0)
            if not self.executar:
                self.coleta_dados.set_sinal("quad:3.0}")
        else:
            self.switch_quad.select(1)

    def get_data_emtry_ampl1(self):
        data = self.emtry_ampl1.get()
        if not self.executar and data.isnumeric():
            self.coleta_dados.set_amplitude(data)
        print(data)
        self.emtry_ampl1.delete(0, len(data))

    def get_data_emtry_freq1(self):
        data = self.emtry_freq1.get()
        if not self.executar and data.isnumeric():
            self.coleta_dados.set_frequencia(data)
        print(data)
        self.emtry_freq1.delete(0, len(data))

    def start_gui(self):
        # Themes: blue (default), dark-blue, green
        ctk.set_default_color_theme("green")
        # image_path = os.path.join(os.path.dirname(
        #                           os.path.realpath(__file__)),
        #                           "utils")
        # self.logo_image = ctk.CTkImage(Image.open(
        #     os.path.join(image_path, "favicon_aeropendulo_png.png")),
        #     size=(26, 26))
        # GUI
        self.root = ctk.CTk()
        self.root.title("Interface Aeropêndulo")
        self.root.geometry("1270x700+40+5")
        if self.tela_fixa:
            self.root.minsize(1270, 700)
            self.root.maxsize(1270, 700)
        self.root.state("normal")

        # +++++++++++++++++++ Frame para adicionar os Menus +++++++++++++++++++
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

        # ++++++++++++++++++++++ Widgets Frame de Menu ++++++++++++++++++++++
        _ = ctk.CTkLabel(master=self.frame_menu, text=" ", width=208)
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

        # button_usb = ctk.CTkButton(master=self.frame_menu, height=30,
        #                            font=ctk.CTkFont(size=15, weight="bold"),
        #                            text="Outra Ação", border_width=1,
        #                            command=self.set_usb_port)
        # button_usb.grid(row=3, column=0, padx=10, pady=4, sticky="w")

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
                                                values=["Light", "Dark"],
                                                command=self.aparencia_event)

        self.aparencia_menu.grid(row=6, column=0, padx=10, pady=4, sticky="w")

        button = ctk.CTkButton(master=self.frame_menu, height=30,
                               font=ctk.CTkFont(size=15, weight="bold"),
                               text="Quit", border_width=1,
                               text_color=("white", "white"),
                               hover_color=("red", "red"),
                               command=self.quit)
        button.grid(row=7, column=0,
                    padx=10, pady=4, sticky="w")

        # +++++++++++++++++ Widgets Frame de Sinais ++++++++++++++++++++++
        self.label_sinais = ctk.CTkLabel(
            master=self.frame_dados,
            text="Informações",
            width=150,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.label_sinais.grid(row=0, column=0, padx=5, pady=3, sticky="s")

        self.label_referencia = ctk.CTkLabel(
            master=self.frame_dados,
            text="Referências: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.label_referencia.grid(row=1, column=0, padx=0, pady=4)

        self.label_referencia1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="20°",
            width=50,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.label_referencia1.grid(row=1, column=1, padx=0, pady=0)

        self.label_angulo = ctk.CTkLabel(
            master=self.frame_dados,
            text="Ângulo: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.label_angulo.grid(row=2, column=0, padx=0, pady=4)

        self.label_angulo1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="23°",
            width=50,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.label_angulo1.grid(row=2, column=1, padx=0, pady=0)

        self.label_controle = ctk.CTkLabel(
            master=self.frame_dados,
            text="Sinal Controle: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            height=25,
            corner_radius=5,
            font=ctk.CTkFont(size=15,
                             weight="normal"))
        self.label_controle.grid(row=3, column=0, padx=0, pady=4)

        self.label_controle1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="23V",
            width=50,
            height=25,
            font=ctk.CTkFont(size=17,
                             weight="bold"))
        self.label_controle1.grid(row=3, column=1, padx=0, pady=0)

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

        # ++++++++++++++++++++ Widgets Frame de Sinais ++++++++++++++++++++++
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
                                        width=65,
                                        font=ctk.CTkFont(size=17,
                                                         weight="bold"),
                                        placeholder_text="(0 à 5)")
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
                                        width=65,
                                        font=ctk.CTkFont(size=17,
                                                         weight="bold"),
                                        placeholder_text="0 à 5")
        self.emtry_freq1.grid(row=2, column=1,
                              padx=(0, 5), pady=4, sticky="s")

        self.btn_offset = ctk.CTkButton(master=self.frame_controle, width=130,
                                        height=30, font=ctk.CTkFont(
                                                    size=15, weight="bold"),
                                        fg_color=("red", "purple"),
                                        text_color=("white", "white"),
                                        hover_color=("#C11C1C", "#4A0255"),
                                        text="Add Offset:", border_width=1,
                                        command=self.get_data_emtry_freq1)
        self.btn_offset.grid(row=3, column=0, padx=5, pady=4, sticky="w")

        self.emtry_offset1 = ctk.CTkEntry(master=self.frame_controle,
                                          width=65,
                                          font=ctk.CTkFont(size=17,
                                                           weight="bold"),
                                          placeholder_text="0 à 5")
        self.emtry_offset1.grid(row=3, column=1,
                                padx=(0, 5), pady=4, sticky="s")

        self.switch_var_deg = ctk.StringVar(value="on")
        self.switch_deg = ctk.CTkSwitch(master=self.frame_controle,
                                        text="Sin. Degrau",
                                        width=40,
                                        switch_height=25,
                                        switch_width=40,
                                        progress_color=("#2CC985", "orange"),
                                        command=self.switch_event_deg,
                                        font=ctk.CTkFont(size=15,
                                                         weight="normal"),
                                        variable=self.switch_var_deg,
                                        onvalue="on", offvalue="off")

        self.switch_deg.grid(row=4, column=0, padx=5, pady=4, sticky="w")

        self.switch_var_quad = ctk.StringVar(value="off")
        self.switch_quad = ctk.CTkSwitch(master=self.frame_controle,
                                         text="Ond. Quad.",
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
        self.switch_seno = ctk.CTkSwitch(master=self.frame_controle,
                                         text="Ond. Seno",
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
        self.root.mainloop()
