# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# Trabalho de Conclusão de Curso - Aeropêndulo
# -----------------------------------------------------
#
# Título : Classe para obter os dados do Microcontrolador via USB
# Professor Orientador: Raphael Teixeira
# Autor: Oséias Farias
#
# Data: 2023
#  ----------------------------------------------------
#

import numpy.typing as npt
from abc import ABC, abstractmethod


class ColetaDadosInterface(ABC):

    @abstractmethod
    def get_dados(self) -> npt.ArrayLike: ...

    @abstractmethod
    def set_amplitude(self, amplitude: str) -> None: ...

    @abstractmethod
    def set_frequencia(self, frequencia: str) -> None: ...

    @abstractmethod
    def set_offset(self, offset: str) -> None: ...

    @abstractmethod
    def set_sinal(self, sinal: str) -> None: ...

    @abstractmethod
    def listar_dir(self) -> None: ...

    @abstractmethod
    def salvar_dados_colhidos(self): ...

    @abstractmethod
    def reconectar(self): ...
