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
    def __init__(self):
        # Objeto para coletar dados do sensor
        self.usb_port = None
        self.baud_rate = 115200

        # Graficos
        self.executar = True
        graficos_sinais = GraficosSinais()
        self.fig, self.ax, self.ln = graficos_sinais.get_fig_axes_ln()

        self.start_gui()
        # self.fila = self.coleta_dados.get_dados()

        # tx = []

    def init(self):
        for i in range(4):
            """tx.append(ax[i].text(40, int(fila[i][-1])+2, f"{fila[i][-1]}",
                                color=[0.3, 0.3, 0.5],
                                fontsize=9,
                                fontweight="bold"))"""
            self.ax[i].set_xlim(0, 50)
            self.ax[i].set_ylim(-15, 15)
            if i > 2:
                self.ax[i].set_xlim(0, 50)
                self.ax[i].set_ylim(-10, 10)
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
                tx[i].set_text(f"{dados[i][-1]:.2f}\nrad/s")"""
            ax.set_xdata(t)
            ax.set_ydata(dados[i])
        return self.ln

    def quit(self):
        self.root.quit()
        self.root.destroy()

    def set_usb_port(self, porta_atual):
        self.usb_port = porta_atual

    @staticmethod
    def aparencia_event(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

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
        self.root.geometry("1270x660+30+45")
        self.root.minsize(1270, 660)
        self.root.maxsize(1270, 660)

        self.frame_menu = ctk.CTkFrame(master=self.root, width=5, height=5)
        self.frame_menu.grid(row=0, column=0, padx=10, pady=10)

        self.frame_graficos = ctk.CTkFrame(master=self.root,
                                           width=5, height=5)
        self.frame_graficos.grid(row=0, column=1, padx=5, pady=10)

        self.label = ctk.CTkLabel(
            self.frame_graficos, text="Interface Aeropêndulo",
            font=ctk.CTkFont(
                size=20, weight="bold")).grid(column=1, row=0)

        self.espaco = ctk.CTkLabel(master=self.frame_menu, text=" ",
                                   width=90)
        self.espaco.grid(row=0, column=0, padx=10, pady=10)

        self.label_nemu = ctk.CTkLabel(master=self.frame_menu, text="Menu",
                                       # image=self.logo_image,
                                       width=90,
                                       font=ctk.CTkFont(size=25,
                                                        weight="bold"))
        self.label_nemu.grid(row=0, column=0, padx=10, pady=10)

        canvas = FigureCanvasTkAgg(self.fig, master=self.frame_graficos)
        canvas.get_tk_widget().grid(column=1, row=1,
                                    padx=5, pady=5)

        button_run = ctk.CTkButton(master=self.frame_menu, height=30,
                                   font=ctk.CTkFont(size=15, weight="bold"),
                                   text="Executar", border_width=1,
                                   command=self.run_graph)
        button_run.grid(row=2, column=0,
                        padx=10, pady=10,
                        sticky="s")

        button_usb = ctk.CTkButton(master=self.frame_menu, height=30,
                                   font=ctk.CTkFont(size=15, weight="bold"),
                                   text="Outra Ação", border_width=1,
                                   command=self.set_usb_port)
        button_usb.grid(row=3, column=0,
                        padx=10, pady=10,
                        sticky="s")

        self.usb_menu = ctk.CTkOptionMenu(
            master=self.frame_menu,
            height=30,
            font=ctk.CTkFont(
                size=15,
                weight="bold"),
            values=["None"],
            command=self.set_usb_port)
        self.usb_menu.grid(row=5, column=0, padx=10, pady=5, sticky="s")

        self.aparencia_menu = ctk.CTkOptionMenu(master=self.frame_menu,
                                                height=30,
                                                font=ctk.CTkFont(
                                                     size=15,
                                                     weight="bold"),
                                                values=["Light", "Dark"],
                                                command=self.aparencia_event)

        self.aparencia_menu.grid(row=6, column=0, padx=10, pady=5, sticky="s")

        button = ctk.CTkButton(master=self.frame_menu, height=30,
                               font=ctk.CTkFont(size=15, weight="bold"),
                               text="Quit", border_width=1,
                               text_color="red", command=self.quit)
        button.grid(row=7, column=0,
                    padx=10, pady=10,
                    sticky="s")

        self.lista_usb = ListaPortasUsb(self.usb_menu, self.set_usb_port)
        self.root.mainloop()
