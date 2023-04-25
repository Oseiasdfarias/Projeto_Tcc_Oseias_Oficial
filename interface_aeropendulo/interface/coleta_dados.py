import serial
from time import sleep
import numpy as np
from threading import Thread
import logging

logger = logging.getLogger(__name__)


class ColetaDados:
    """Coleta os dados do Aeropêndulo para plotagem.

    param: porta='/dev/ttyUSB0'
    param: baud_rate=115200

    """
    def __init__(self, porta="/dev/ttyUSB0", baud_rate=115200):
        self.porta = porta
        self.baud_rate = baud_rate
        self.fila = np.array([[], [], [], [], [], []]).astype(object)
        self.__init_thread()

    def get_dados(self):
        return self.fila

    def set_amplitude(self, amplitude):
        data = f"ampl:{amplitude}"
        print(data)
        self.disp.write(data.encode("utf8"))

    def set_frequencia(self, frequencia):
        data = f"freq:{frequencia}"
        print(data)
        self.disp.write(data.encode("utf8"))

    def set_offset(self, offset):
        data = f"offset:{offset}"
        self.disp.write(data.encode("utf8"))

    def set_sinal(self, sinal):
        self.disp.write(sinal.encode("utf8"))
        print(f"Sinal Configurado: {sinal}")

    def __init_thread(self):
        self.new_thread = Thread(target=self.__coleta_dados)
        self.new_thread.daemon = True
        self.new_thread.start()

    def __coleta_dados(self):
        self.disp = serial.Serial(self.porta, self.baud_rate)
        con1 = f"\nConectando!!! >> ID: {self.porta}, "
        con2 = f"BaudRate: {self.baud_rate}"
        print(con1 + con2)
        if self.disp.isOpen():
            print(f"Conectado com Sucesso!!! >> ID: {self.porta}\n")
        self.disp.parity = "O"
        self.disp.bytesize = 7

        self.disp.reset_input_buffer()

        while True:
            try:
                # if (self.disp.inWaiting() > 0):
                dado = self.disp.readline()
                dados1 = str(dado.decode('utf8')).rstrip("\n")
                dados1 = dados1.split(",")

                try:
                    dados_float = np.array([dados1], dtype="float64").T
                    if len(self.fila[0]) <= 50:
                        self.fila = np.append(self.fila,
                                              dados_float, axis=1)
                    else:
                        self.fila = np.delete(self.fila, np.s_[:1], 1)
                except Exception as erro1:
                    print(f"Erro: {erro1}")
                    sleep(0.03)
            except serial.SerialException:
                print("erro de leitura")

            if not self.disp.isOpen():
                try:
                    self.disp.close()
                    self.disp = serial.Serial(self.porta, self.baud_rate)
                    print(f"\nReconectando!!! >> ID: {self.porta}")
                    if self.disp.isOpen():
                        self.disp.reset_input_buffer()
                        print(f"Reconectado!!! >> ID: {self.porta}\n")
                    sleep(1)
                except serial.SerialException:
                    pass
                    # logger.exception(e)
