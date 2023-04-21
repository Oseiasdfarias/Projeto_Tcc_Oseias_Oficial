# -*- coding: utf-8 -*-
"""
Bancada de Controle de velocidade: Motor-Gerador
UFPA - Campus Tucuruí
Monitoria de Sistemas de Controle para Engenharia - PGRAD - MONITORIA 03/2020
Coodenador: Cleison Daniel Silva
Bolsista: Felipe Silveira Piano
Data: 28/09/2020
"""

import serial
import numpy as np
import matplotlib.pyplot as plt
import time as t
from scipy.signal import square,sawtooth


numAmostras = 300
tempo = np.zeros(numAmostras)
y = np.zeros(numAmostras)
Ts = 0.0291
fre = 0.25
Amplitude = 0.25
setpoint = 1.5
u = np.zeros(numAmostras)
r = np.zeros(numAmostras)
toc = np.zeros(numAmostras)
I = np.ones(numAmostras)
kp = 1.3
ki = 0.2

print('\nEstabelecendo conexão.')
conexao = serial.Serial(port='COM3', baudrate=9600, timeout=0.005)
t.sleep(1)
print('\nIniciando coleta.')


for n in range(numAmostras):
    tic = t.time()
    
    r[n] = Amplitude*square(2*np.pi*fre*n*Ts) + setpoint
    #r[n] = Amplitude*np.sin(2*np.pi*fre*n*Ts) + setpoint
    
    
    if (conexao.inWaiting() > 0):
        y[n] = conexao.readline().decode()
    
    #Controlador
    erro = r[n] - y[n]
    if (n > 0):
        I[n] = I[n-1] + ki*erro    
    u[n] = kp*erro + I[n]
    
    conexao.write(str(round(u[n]*255/5)).encode())
    
    t.sleep(0.02)
    
    if (n > 0):
        tempo[n] = tempo[n-1] + Ts
    toc[n] = t.time() - tic
    
       
conexao.write('0'.encode())
print('\nFim da coleta.')
conexao.close()


plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(tempo,r,'-b',tempo,y,'-r',linewidth=0.8)
plt.xlabel('tempo(s)')
plt.ylabel('Tensão (V)')
plt.title('Onda Quadrada - Malha fechada')
plt.legend(loc='lower right', labels=('Sinal de Entrada','Sinal de Saída'))
plt.subplot(2,1,2)
plt.plot(tempo,u,'-k',linewidth=0.8)
plt.xlabel('tempo(s)')
plt.ylabel('Tensão (V)')
plt.title('Sinal de Controle')
plt.subplots_adjust(hspace=0.5)
plt.show()