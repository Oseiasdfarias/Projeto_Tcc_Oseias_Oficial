import serial
from time import sleep
from queue import Queue

queue_: Queue = Queue(maxsize=3)


def serialRead(serialPort, queue):
    """Adds serial port input to a queue."""

    n = [63, 343, 1212, 1332, 2343, 2354]

    ser = serial.Serial(serialPort,
                        baudrate=115200,
                        timeout=0.005,
                        parity=serial.PARITY_ODD,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS)
    ser.reset_input_buffer()
    sleep(1)
    i = 0
    while True:
        data = f"{round(n[i])}"
        print(data)
        try:
            if not ser.isOpen():
                print("Desconectado!!!")
                ser = serial.Serial(baudrate=115200,
                                    timeout=0.005,
                                    parity=serial.PARITY_ODD,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS)

                print("Reconnecting")
            # data = input("Digite o dado:")
            ser.write(data.encode("utf-8"))
            ser.flush()
            sleep(0.4)
            dados = ser.readline()
            ser.flush()
            sleep(0.4)
            print(str(dados.decode('utf-8')).rstrip("\n"))
            i += 1
            if (i >= 5):
                i = 0
        except Exception:
            try:
                ser.close()
                ser = serial.Serial(baudrate=115200,
                                    timeout=0.005,
                                    parity=serial.PARITY_ODD,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS)
                ser.reset_input_buffer()
            except Exception:
                pass
            sleep(1)


if __name__ == "__main__":
    serialRead("/dev/ttyUSB0", queue_)
