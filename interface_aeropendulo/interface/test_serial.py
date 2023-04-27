import serial
from time import sleep
from queue import Queue

queue_: Queue = Queue(maxsize=3)


def serialRead(serialPort, queue):
    """Adds serial port input to a queue."""

    n = 63.0
    data = f"{round(n)}"

    ser = serial.Serial(serialPort,
                        baudrate=9600,
                        timeout=0.005,
                        parity=serial.PARITY_ODD,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS)
    ser.reset_input_buffer()
    # ser.parity = "O"
    # ser.bytesize = 7
    sleep(1)

    while True:
        try:
            if not ser.isOpen():
                print("Desconectado!!!")
                ser = serial.Serial(serialPort, baudrate=9600, timeout=0.005)

                ser.parity = "O"
                ser.bytesize = 7

                print("Reconnecting")
            # data = input("Digite o dado:")
            ser.write(data.encode("utf-8"))
            sleep(0.2)
            dados = ser.readline()
            ser.flush()
            sleep(0.2)
            print(str(dados.decode('utf-8')).rstrip("\n"))
            n += 1.2
            data = f"{round(n)}"
        except Exception:
            try:
                ser.close()
                ser = serial.Serial(serialPort, baudrate=9600, timeout=0.005)
                ser.reset_input_buffer()
            except Exception:
                pass
            sleep(1)


if __name__ == "__main__":
    serialRead("/dev/ttyUSB0", queue_)
