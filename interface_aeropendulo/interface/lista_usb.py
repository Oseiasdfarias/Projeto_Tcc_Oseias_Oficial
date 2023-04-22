import serial.tools.list_ports as ports_usb


def listar_portas_usb():
    lista_usb = [usb for usb in ports_usb.comports()]
    return lista_usb


if __name__ == "__main__":
    print(listar_portas_usb())
