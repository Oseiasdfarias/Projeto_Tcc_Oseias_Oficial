# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para listagem de Portas USB Disponíveis
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

from abc import ABC, abstractmethod


class ListaPortasUsb(ABC):

    @abstractmethod
    def listar_portas_usb(self): ...

    @abstractmethod
    def atualizar_dados_menu(self): ...
