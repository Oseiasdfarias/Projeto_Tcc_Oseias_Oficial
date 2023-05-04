# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Script usado para testar a interface USB
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

import serial
from time import sleep
from queue import Queue

queue_: Queue = Queue(maxsize=3)


def serialRead(serialPort, queue):
    """Adds serial port input to a queue."""

    n = 990.23
    # data = f"{round(n)}"
    data = f"{n:.2f}"
    ser = serial.Serial(serialPort, baudrate=115200, timeout=0.005)

    ser.reset_input_buffer()
    sleep(1)

    while True:
        try:
            if not ser.isOpen():
                print("Desconectado!!!")
                ser = serial.Serial(serialPort, baudrate=115200, timeout=0.005)

                ser.reset_input_buffer()
                ser.flush()

                print("Reconnecting")
            ser.write(data.encode("utf-8"))
            ser.flush()
            sleep(0.01)
            dados = ser.readline()
            ser.flush()
            sleep(0.01)
            print(str(dados.decode('utf-8')).rstrip("\n"))
            n += 1.2
            # data = f"{round(n)}"
            data = f"{n:.2f}"
        except Exception:
            try:
                print("testestestsert")
                ser.close()
                ser = serial.Serial(serialPort, baudrate=115200, timeout=0.005)
                ser.reset_input_buffer()
            except Exception:
                pass
            sleep(1)


if __name__ == "__main__":
    serialRead("/dev/ttyUSB0", queue_)
