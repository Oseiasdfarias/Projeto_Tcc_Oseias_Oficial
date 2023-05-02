"""*************************  | |  ****************************
      * Universidade Federal do Pará
      * Campus Universitário de Tucuruí
      * Faculdade de Engenharia Elétrica
      * Trabalho de Conclusão de Curso - Aeropêndulo

      * Título : Firmware Potótipo Aeropêndulo
      * Professor Orientador: Raphael Teixeira
      * Autor  : Oséias Farias

      * Arquivo: main.cpp    |   Data: 2023
           ***************   |   ***************"""

import serial.tools.list_ports as ports_usb
from pyudev import Context, Monitor
from threading import Thread


class ListaPortasUsb(object):
    """Classe responsável por obter as portas USBs dos Microcontroladores
    plugados no Computador.

    param: atualiza_menu - Atualiza o menu de opções com as portas disponíveis
            no monento.
    param: set_porta_atual - Atualiza a variável usada para salvar a porta a
            ser usada no momento da conexão da interface com o dispositivo.

    """
    def __init__(self, atualiza_menu, set_porta_atual) -> None:
        self.set_porta_atual = set_porta_atual
        self.atualiza_menu = atualiza_menu
        self.monitora_conexao_usb = self.listar_portas_usb()
        self.atualizar_dados_menu()
        self.__init_thread()

    def listar_portas_usb(self):
        """Lista os microcontroladores conectados ao Computador.

        """
        lista_usb = [usb.device for usb in ports_usb.comports()]
        return lista_usb

    def __init_thread(self):
        """Inicia uma thread para executar o métido __monitora_usb_conexao().

        """
        self.new_thread = Thread(target=self.__monitora_usb_conexao)
        self.new_thread.daemon = True
        self.new_thread.start()

    def __monitora_usb_conexao(self):
        """Monitora a conexão e desconexão de dispositivo USB do computador.
        """
        ctx = Context()
        monitor = Monitor.from_netlink(ctx)
        monitor.filter_by(subsystem='usb')

        for device in iter(monitor.poll, None):
            if device.action == 'add' or 'remove':
                self.atualizar_dados_menu()
                print(f"USB Conectado!!! : {self.monitora_conexao_usb}")

    def atualizar_dados_menu(self):
        """Atualiza as informações do menu na interface.

        """
        self.monitora_conexao_usb = self.listar_portas_usb()
        if self.monitora_conexao_usb != []:
            self.atualiza_menu.configure(
                values=self.monitora_conexao_usb)
            self.atualiza_menu.set(self.monitora_conexao_usb[0])
            self.set_porta_atual(self.monitora_conexao_usb[0])
        else:
            self.atualiza_menu.configure(
                values=["Sem Disp."])
            self.atualiza_menu.set("Sem Disp.")
            self.set_porta_atual(None)
