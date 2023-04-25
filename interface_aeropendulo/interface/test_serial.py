import serial
from time import sleep
from queue import Queue

queue_: Queue = Queue(maxsize=3)

def serialRead(serialPort, queue):
    """Adds serial port input to a queue."""

    n = 0.0
    data = f"ampl,{n}"

    ser = serial.Serial(serialPort, 115200)

    ser.parity = "O"
    ser.bytesize = 7

    while True:
        try:
            if not ser.isOpen():
                print("Desconectado!!!")
                ser = serial.Serial(serialPort, 115200)

                # ser.parity = "O"
                # ser.bytesize = 7

                print("Reconnecting")
            # data = input("Digite o dado:")
            #ser.write(data.encode("utf8"))
            sleep(0.5)
            dados = ser.readline()
            print(str(dados.decode('utf8')).rstrip("\n"))
            n += 1.0
            data = f"ampl,{n}"
        except Exception:
            try:
                ser.close()
                ser = serial.Serial(serialPort, 115200)
                ser.reset_input_buffer()
            except Exception:
                pass
            sleep(1)


if __name__ == "__main__":
    serialRead("/dev/ttyUSB1", queue_)
