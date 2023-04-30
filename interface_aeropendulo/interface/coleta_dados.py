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
        data = ((float(amplitude)*1000.)/15.) + 1000.
        data = f"{int(data)}"
        print(f"Ampl.: {data}")
        self.disp.reset_input_buffer()
        for i in range(100):
            self.disp.write(data.encode("utf-8"))
            sleep(0.01)
            self.disp.flush()

    def set_frequencia(self, frequencia):
        data = ((float(frequencia)*1000.)/15.) + 2000.
        data = f"{int(data)}"
        print(f"Freq.: {data}")
        self.disp.reset_input_buffer()
        for i in range(100):
            self.disp.write(data.encode("utf-8"))
            sleep(0.01)
            self.disp.flush()

    def set_offset(self, offset):
        data = ((float(offset)*1000.)/15.) + 3000.
        data = f"{int(data)}"
        print(f"Offset: {data}")
        self.disp.reset_input_buffer()
        for i in range(100):
            self.disp.write(data.encode("utf-8"))
            sleep(0.01)
        self.disp.flush()

    def set_sinal(self, sinal):
        self.disp.write(sinal.encode("utf-8"))
        self.disp.flush()
        print(f"Sinal Configurado: {sinal}")

    def __init_thread(self):
        self.new_thread = Thread(target=self.__coleta_dados)
        self.new_thread.daemon = True
        self.new_thread.start()

    def __coleta_dados(self):
        self.disp = serial.Serial(self.porta,
                                  self.baud_rate,
                                  timeout=0.005)
        con1 = f"\nConectando!!! >> ID: {self.porta}, "
        con2 = f"BaudRate: {self.baud_rate}"
        print(con1 + con2)
        if self.disp.isOpen():
            print(f"Conectado com Sucesso!!! >> ID: {self.porta}\n")
        # self.disp.reset_input_buffer()

        while True:
            try:
                # if (self.disp.inWaiting() > 0):
                dado = self.disp.readline()
                # self.disp.flush()
                dados1 = str(dado.decode('utf-8')).rstrip("\n")
                dados1 = dados1.split(",")
                if dados1 == ['']:
                    continue

                try:
                    dados_float = np.array([dados1], dtype="float64").T
                    if len(self.fila[0]) <= 50:
                        self.fila = np.append(self.fila,
                                              dados_float, axis=1)
                    else:
                        self.fila = np.delete(self.fila, np.s_[:1], 1)
                    sleep(0.02)
                except Exception as erro1:
                    print(f"Erro: {erro1}")
                    sleep(0.02)
            except serial.SerialException:
                print("erro de leitura")

            if not self.disp.isOpen():
                try:
                    self.disp.close()
                    self.disp = serial.Serial(self.porta,
                                              self.baud_rate,
                                              timeout=0.005)
                    print(f"\nReconectando!!! >> ID: {self.porta}")
                    if self.disp.isOpen():
                        self.disp.flush()
                        print(f"Reconectado!!! >> ID: {self.porta}\n")
                    sleep(1)
                except serial.SerialException:
                    pass
                    # logger.exception(e)
