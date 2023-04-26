import serial
from time import sleep
from queue import Queue

queue_: Queue = Queue(maxsize=3)


def serialRead(serialPort, queue):
    """Adds serial port input to a queue."""

    n = 0.00
    data = f"ampl,{n:.2f}"

    ser = serial.Serial(serialPort, 115200)
    ser.reset_input_buffer()
    ser.parity = "O"
    ser.bytesize = 7

    while True:
        try:
            if not ser.isOpen():
                print("Desconectado!!!")
                ser = serial.Serial(serialPort, 115200)

                ser.parity = "O"
                ser.bytesize = 7

                print("Reconnecting")
            # data = input("Digite o dado:")
            ser.write(data.encode("utf-8"))
            ser.flush()
            sleep(0.2)
            dados = ser.readline()
            ser.flush()
            sleep(0.1)
            print(str(dados.decode('utf-8')).rstrip("\n"))
            n += 1.0
            data = f"ampl,{n:.2f}"
        except Exception:
            try:
                ser.close()
                ser = serial.Serial(serialPort, 115200)
                ser.reset_input_buffer()
            except Exception:
                pass
            sleep(1)


if __name__ == "__main__":
    serialRead("/dev/ttyUSB0", queue_)
