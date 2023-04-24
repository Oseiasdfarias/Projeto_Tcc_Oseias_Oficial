import serial
from time import sleep
from queue import Queue

queue_: Queue = Queue(maxsize=3)


def serialRead(serialPort, queue):
    """Adds serial port input to a queue."""

    ser = serial.Serial(serialPort, 115200)

    ser.parity = "O"
    ser.bytesize = 7

    while True:
        try:
            print("aqui")
            if not ser.isOpen():
                print("aqui2")
                ser = serial.Serial(serialPort, 115200)

                # ser.parity = "O"
                # ser.bytesize = 7

                print("Reconnecting")

            queue.put(ser.read(27))
            ser.write(chr(6).encode())

            print("Writing Data...")
            dados = ser.readline()
            print(str(dados.decode('utf8')).rstrip("\n"))
        except Exception:
            try:
                ser.close()
                print("aqui3")
                ser = serial.Serial(serialPort, 115200)
                ser.reset_input_buffer()
            except Exception:
                print()

            # if not ser==None:
            #    ser.close()
            #    ser = None
            # print("Disconnecting")

            # print("No Connection")
            sleep(2)


if __name__ == "__main__":
    serialRead("/dev/ttyUSB0", queue_)
