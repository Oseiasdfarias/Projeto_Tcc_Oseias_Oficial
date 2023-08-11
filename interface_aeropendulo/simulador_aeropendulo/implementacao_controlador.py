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

class ControladorDiscreto:
    """
        Classe que implementa os controladores para o sistema.
        Args:
            referencia: int - Sinal de referência para o controlador seguir.
            T: Período de amostragem do controlador.
        Return:
            None
    """
    def __init__(self, referencia: int = 1, T: float = 0.0625) -> None:
        self.uk = 0
        self.uk1 = 0
        self.ek = 0
        self.ek1 = 0
        self.yout = 0
        self.k = 0
        self.r = referencia
        self.T = T

    # Pega o sinal do sensor
    def set_sensor(self, yout: float = 1) -> None:
        """
            Recebe o sinal de saída, o ângulo do braço do aeropêndulo.
        Args:
            yout: Sinal do sensor de ângulo.
        Return:
            None
        """
        self.yout = yout

    # disponibiliza o sinal de controle
    def get_u(self) -> float:
        """
            Método que retorna o sinal de controle.
        Return:
            float: Sinal de controle.
        """
        return self.uk

    # Calcula o sinal de controle Proporcional Integral.
    def control_pi(self) -> None:
        """
            Método que implementa o controle Proporcional Integral
            discretizado.
        Return:
            None
        """
        self.ek = self.r - self.yout
        self.uk = self.uk1 + 0.2165 * self.ek - 0.2087 * self.ek1
        self.ek1 = self.ek
        self.uk1 = self.uk
        self.k = self.k + 1

    def controle_proporcional(self, kp=1.0):
        """
            Método que implementa o controle Proporcional discretizado.
        Args:
            kp: Ganho do controlador Proporcional.
        Return:
            None
        """
        self.ek = self.r - self.yout
        self.KP = kp
        self.uk = self.KP * self.ek
