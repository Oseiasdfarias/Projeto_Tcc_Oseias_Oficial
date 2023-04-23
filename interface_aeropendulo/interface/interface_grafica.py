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
            self.ax[i].axhline(0, color="dimgray", lw=1.2)
            self.ax[i].axvline(0.5, color="dimgray", lw=1.2)
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

        # ------- Frame para adicionar os Menus -------
        self.frame_menus = ctk.CTkFrame(master=self.root, width=5, height=5)
        self.frame_menus.grid(row=0, column=0, padx=10, pady=10, sticky="sn")

        self.frame_menu = ctk.CTkFrame(master=self.frame_menus,
                                       width=5, height=5)
        self.frame_menu.grid(row=2, column=0, padx=10, pady=10, sticky="s")

        self.frame_dados = ctk.CTkFrame(master=self.frame_menus,
                                        width=5, height=10)
        self.frame_dados.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.frame_controle = ctk.CTkFrame(master=self.frame_menus,
                                           width=5, height=10)
        self.frame_controle.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # ------- Frame para adicionar os gráficos -------
        self.frame_graficos = ctk.CTkFrame(master=self.root,
                                           width=5, height=5)
        self.frame_graficos.grid(row=0, column=1, padx=5, pady=10, sticky="s")

        self.label = ctk.CTkLabel(
            self.frame_graficos, text="Interface Aeropêndulo",
            font=ctk.CTkFont(
                size=25, weight="bold")).grid(column=1, row=0)

        # ------- Widgets Frame de Menu -------
        self.label_nemu = ctk.CTkLabel(master=self.frame_menu, text="Menu",
                                       # image=self.logo_image,
                                       width=188,
                                       font=ctk.CTkFont(size=25,
                                                        weight="bold"))
        self.label_nemu.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        canvas = FigureCanvasTkAgg(self.fig, master=self.frame_graficos)
        canvas.get_tk_widget().grid(column=1, row=1,
                                    padx=5, pady=5, sticky="sn")

        button_run = ctk.CTkButton(master=self.frame_menu, height=30,
                                   font=ctk.CTkFont(size=17, weight="bold"),
                                   text="Executar", border_width=1,
                                   command=self.run_graph)
        button_run.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        button_usb = ctk.CTkButton(master=self.frame_menu, height=30,
                                   font=ctk.CTkFont(size=17, weight="bold"),
                                   text="Outra Ação", border_width=1,
                                   command=self.set_usb_port)
        button_usb.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.usb_menu = ctk.CTkOptionMenu(
            master=self.frame_menu,
            height=30,
            font=ctk.CTkFont(
                size=17,
                weight="bold"),
            values=["None"],
            command=self.set_usb_port)
        self.usb_menu.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.aparencia_menu = ctk.CTkOptionMenu(master=self.frame_menu,
                                                height=30,
                                                font=ctk.CTkFont(
                                                     size=17,
                                                     weight="bold"),
                                                values=["Light", "Dark"],
                                                command=self.aparencia_event)

        self.aparencia_menu.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        button = ctk.CTkButton(master=self.frame_menu, height=30,
                               font=ctk.CTkFont(size=17, weight="bold"),
                               text="Quit", border_width=1,
                               text_color=("white", "white"),
                               command=self.quit)
        button.grid(row=7, column=0,
                    padx=10, pady=5, sticky="w")

        # ------- Widgets Frame de Sinais -------
        self.label_sinais = ctk.CTkLabel(
            master=self.frame_dados,
            text="Informações",
            width=150,
            font=ctk.CTkFont(size=25,
                             weight="bold"))
        self.label_sinais.grid(row=0, column=0, padx=5, pady=3, sticky="s")

        self.label_referencia = ctk.CTkLabel(
            master=self.frame_dados,
            text="Referências: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            corner_radius=5,
            font=ctk.CTkFont(size=17,
                             weight="normal"))
        self.label_referencia.grid(row=1, column=0, padx=0, pady=4)

        self.label_referencia1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="20°",
            width=50,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.label_referencia1.grid(row=1, column=1, padx=0, pady=0)

        self.label_angulo = ctk.CTkLabel(
            master=self.frame_dados,
            text="Ângulo: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            corner_radius=5,
            font=ctk.CTkFont(size=17,
                             weight="normal"))
        self.label_angulo.grid(row=2, column=0, padx=0, pady=4)

        self.label_angulo1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="23°",
            width=50,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.label_angulo1.grid(row=2, column=1, padx=0, pady=0)

        self.label_controle = ctk.CTkLabel(
            master=self.frame_dados,
            text="Sinal Controle: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            corner_radius=5,
            font=ctk.CTkFont(size=17,
                             weight="normal"))
        self.label_controle.grid(row=3, column=0, padx=0, pady=4)

        self.label_controle1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="23V",
            width=50,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.label_controle1.grid(row=3, column=1, padx=0, pady=0)

        self.label_erro = ctk.CTkLabel(
            master=self.frame_dados,
            text="Sinal de Erro: ",
            text_color=("white", "white"),
            fg_color=("purple", "red"),
            width=140,
            corner_radius=5,
            font=ctk.CTkFont(size=17,
                             weight="normal"))
        self.label_erro.grid(row=4, column=0, padx=0, pady=4)

        self.label_erro1 = ctk.CTkLabel(
            master=self.frame_dados,
            text="15°",
            width=50,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.label_erro1.grid(row=4, column=1, padx=0, pady=2)

        # ------- Widgets Frame de Sinais -------
        self.label_nemu = ctk.CTkLabel(master=self.frame_controle,
                                       text="Sinal de Ref.",
                                       width=150,
                                       font=ctk.CTkFont(size=25,
                                                        weight="bold"))
        self.label_nemu.grid(row=0, column=0, padx=5, pady=5)
        self.teste = ctk.CTkLabel(
            master=self.frame_controle,
            text="Sinal de Erro: ",
            text_color=("white", "white"),
            fg_color=("blue", "orange"),
            width=140,
            corner_radius=5,
            font=ctk.CTkFont(size=17,
                             weight="normal"))
        self.teste.grid(row=1, column=0, padx=0, pady=4)

        self.teste1 = ctk.CTkLabel(
            master=self.frame_controle,
            text="15°",
            width=50,
            font=ctk.CTkFont(size=20,
                             weight="bold"))
        self.teste1.grid(row=1, column=1, padx=0, pady=2)

        self.lista_usb = ListaPortasUsb(self.usb_menu, self.set_usb_port)
        self.root.mainloop()
