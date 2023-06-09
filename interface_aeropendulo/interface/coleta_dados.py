# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para obter os dados do Microcontrolador via USB
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

import serial
from time import sleep
import numpy as np
import pandas as pd
from threading import Thread
import datetime as dt
import os
import logging
import numpy.typing as npt

logger = logging.getLogger(__name__)


class ColetaDados:
    """Coleta os dados do Aeropêndulo para plotagem.

    param: porta='/dev/ttyUSB0'
    param: baud_rate=115200

    """
    def __init__(self, amostras: int = 50, porta: str = "/dev/ttyUSB0",
                 baud_rate: int = 115200) -> None:
        self.amostras = amostras
        self.flag_salvar_dados = False
        os.chdir("interface")
        self.porta = porta
        self.baud_rate = baud_rate
        self.fila: npt.ArrayLike = np.array(
            [[], [], [], [], [], [], []]).astype(object)
        self.salvar_dados: npt.ArrayLike = np.array(
            [[], [], [], [], [], [], []]).astype(object)
        self.dados_atuais = None
        self.__init_thread()

    def get_dados(self) -> npt.ArrayLike:
        return self.fila

    def set_amplitude(self, amplitude: str) -> None:
        data = ((float(amplitude)*1000.)/30.) + 1000.
        data_conv = f"{int(data)}"
        print(f"Ampl.: {data_conv}")
        self.disp.reset_input_buffer()
        if self.disp.write(data_conv.encode("utf-8")):
            self.disp.flush()
            return
        else:
            sleep(0.01)
            self.disp.flush()
            self.set_amplitude(amplitude)

    def set_frequencia(self, frequencia: str) -> None:
        print(f"Dado entrada freq: {float(frequencia)}")
        data = ((float(frequencia)*1000.)/5.) + 2000.
        data_conv = f"{int(data)}"
        print(f"Freq.: {data_conv}")
        self.disp.reset_input_buffer()
        if self.disp.write(data_conv.encode("utf-8")):
            self.disp.flush()
            return
        else:
            sleep(0.01)
            self.disp.flush()
            self.set_frequencia(frequencia)

    def set_offset(self, offset: str) -> None:
        data = ((float(offset)*1000.)/120.) + 3000.
        data_conv = f"{int(data)}"
        print(f"Offset: {data_conv}")
        self.disp.reset_input_buffer()
        if self.disp.write(data_conv.encode("utf-8")):
            self.disp.flush()
            return
        else:
            sleep(0.01)
            self.disp.flush()
            self.set_offset(offset)

    def set_sinal(self, sinal: str) -> None:
        self.disp.reset_input_buffer()
        if self.disp.write(sinal.encode("utf-8")):
            self.disp.flush()
            print(f"Sinal Configurado: {sinal}")
        else:
            sleep(0.01)
            self.disp.flush()
            self.set_sinal(sinal)

    def listar_dir(self) -> None:
        pastas = os.listdir()
        diretorio = "dados_de_ensaio"
        file = False
        if not (os.getcwd().split("/")[-1] == diretorio):
            for i in pastas:
                if (i == diretorio):
                    file = True
            if file:
                os.chdir(diretorio)
            else:
                os.mkdir(diretorio)
                os.chdir(diretorio)

    def salvar_dados_colhidos(self):
        data = dt.datetime.now()
        nome1 = f"{data.day}_{data.month}_{data.year}"
        nome2 = f"_{data.hour}_{data.minute}_{data.second}"
        self.nome_arquivo = f"arquivo_{nome1 + nome2}.csv"
        self.listar_dir()
        dt_dados_obtidos = pd.DataFrame(self.salvar_dados.T)
        dt_dados_obtidos.to_csv(self.nome_arquivo)
        dt_dados_obtidos = None
        self.disp.flush()
        self.disp.reset_input_buffer()

    def __init_thread(self) -> None:
        self.new_thread = Thread(target=self.__coleta_dados)
        self.new_thread.daemon = True
        self.new_thread.start()

    def reconectar(self):
        try:
            self.disp.close()
            self.disp = serial.Serial(self.porta,
                                      self.baud_rate,
                                      timeout=0.005)
            print(f"\nReconectando!!! >> ID: {self.porta}")
            if self.disp.is_open:
                self.disp.reset_input_buffer()
                self.disp.flush()
                print(f"Reconectado!!! >> ID: {self.porta}\n")
            sleep(1)
        except serial.SerialException:
            pass
            # logger.exception(e)

    def __coleta_dados(self):
        self.disp = serial.Serial(self.porta,
                                  self.baud_rate,
                                  timeout=0.005)
        con1 = f"\nConectando!!! >> ID: {self.porta}, "
        con2 = f"BaudRate: {self.baud_rate}"
        print(con1 + con2)
        if self.disp.is_open:
            print(f"Conectado com Sucesso!!! >> ID: {self.porta}\n")
        print(f"Configurações:\n{self.disp.get_settings()}")
        while True:
            try:
                dado = self.disp.readline()
                self.disp.reset_output_buffer()
                self.disp.flush()
                dados1 = str(dado.decode('utf-8')).rstrip("\n")
                dados1 = dados1.split(",")
                if dados1 == ['']:
                    continue
                try:
                    dados_float = np.array([dados1], dtype="float64").T
                    # print(dados_float)
                    if len(self.fila[0]) <= self.amostras:
                        self.fila = np.append(self.fila,
                                              dados_float, axis=1)
                    else:
                        self.fila = np.delete(self.fila, np.s_[:1], 1)
                    if self.flag_salvar_dados:
                        self.salvar_dados = np.append(self.salvar_dados,
                                                      dados_float, axis=1)
                    self.dados_atuais = dados_float
                except Exception as erro1:
                    print(f"Erro: {erro1}")
                    sleep(0.02)
            except serial.SerialException:
                print("erro de leitura")
                self.reconectar()

            if not self.disp.is_open:
                self.reconectar()
