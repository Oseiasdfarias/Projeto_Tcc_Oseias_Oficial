# -*- coding: utf-8 -*-
"""
Bancada de Controle de velocidade: Motor-Gerador
UFPA - Campus Tucuruí
Monitoria de Sistemas de Controle para Engenharia - PGRAD - MONITORIA 03/2020
Coodenador: Cleison Daniel Silva
Bolsista: Felipe Silveira Piano / Flávio Stoitchkov Santos
Data: 01/12/2020
"""

import serial
import numpy as np
import matplotlib.pyplot as plt
import time as t
from scipy.signal import square,sawtooth


numAmostras = 400
tempo = np.zeros(numAmostras)
y = np.zeros(numAmostras)
Ts = 0.0206
fre = 0.25
Amplitude = 0.25
setpoint = 1.5
u = np.zeros(numAmostras)
r = np.zeros(numAmostras)
toc = np.zeros(numAmostras)
kp = 1.5

for n in range(numAmostras):
    r[n] = Amplitude*square(2*np.pi*fre*n*Ts) + setpoint
    #r[n] = Amplitude*np.sin(2*np.pi*fre*n*Ts) + setpoint
    #r[n] = u[n]

print('\nEstabelecendo conexão.')
conexao = serial.Serial(port='COM3', baudrate=9600, timeout=0.005)
t.sleep(1)
print('\nIniciando coleta.')


for n in range(numAmostras):
    tic = t.time()
    
    
    if (conexao.inWaiting() > 0):
        y[n] = conexao.readline().decode()
    
    #Controlador
    erro = r[n] - y[n]
    if (n > 0):  
        u[n] = kp*erro
    
    conexao.write(str(round(u[n]*255/5)).encode())
    
    t.sleep(0.02)
    
    if (n > 0):
        tempo[n] = tempo[n-1] + Ts
    toc[n] = t.time() - tic
    
       
conexao.write('0'.encode())
print('\nFim da coleta.')
conexao.close()


plt.figure(figsize=(10,6))
plt.plot(tempo,r,'-b',tempo,y,'-r',linewidth=0.8)
plt.xlabel('tempo(s)')
plt.ylabel('Tensão (V)')
plt.title('Onda Quadrada')
plt.legend(loc='lower right', labels=('Sinal de Entrada','Sinal de Saída'))
