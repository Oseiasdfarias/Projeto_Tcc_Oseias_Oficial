# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# -----------------------------------------------------
#
# Laboratório Virtual Sistemas Dinâmicos e Controle
# Tema: Simulação Aeropêndulo
# Autor: Oséias Farias
# Orientadores: Prof. Dr: Raphael Teixeira,
#               Prof. Dr: Rafael Bayma
#
# Data: 2023
#  ----------------------------------------------------
#
from abc import ABC, abstractmethod


class AnimacaoAeropenduloInterface(ABC):

    @abstractmethod
    def pause_giro(self) -> None: ...

    @abstractmethod
    def girar_helice(self) -> None: ...

    @abstractmethod
    def set_posicao_helice(self, angle): ...

    @abstractmethod
    def update_helice(self, angle, ts) -> None: ...
