"""
Bancada Motor-Gerador
UFPA - Campus Tucuruí
Monitoria de Sistemas de Controle para Engenharia - PGRAD - MONITORIA 03/2020
Coodenador: Cleison Daniel Silva
Bolsista: Felipe Silveira Piano
Data: 27/09/2020
"""

import serial
import numpy as np
import matplotlib.pyplot as plt
import time as t
from scipy.signal import square,sawtooth

numAmostras = 600
tempo = np.zeros(numAmostras)
y = np.zeros(numAmostras)
Ts = 0.02
fre = 0.25
Amplitude = 0.25
setpoint = 2.75
a = np.zeros(int(numAmostras/2))
b = 4*np.ones(int(numAmostras/2))
u = np.concatenate([a,b]) #degrau
r = np.zeros(numAmostras)
toc = np.zeros(numAmostras)

for n in range(numAmostras):
    #r[n] = Amplitude*square(2*np.pi*fre*n*Ts) + setpoint
    #r[n] = Amplitude*sawtooth(2*np.pi*fre*n*Ts) + setpoint
    r[n] = Amplitude*np.sin(2*np.pi*fre*n*Ts) + setpoint
    #r[n] = u[n]
    
print('\nEstabelecendo conexão.')
conexao = serial.Serial(port='COM3', baudrate=38400, timeout=0.005)
t.sleep(1)
print('\nIniciando coleta.')

for n in range(numAmostras):
    tic = t.time()

    if (conexao.inWaiting() > 0):
        y[n] = conexao.readline().decode()
           
    conexao.write(str(round(r[n]*255/5)).encode())
    
    t.sleep(0.02)
    
    if (n > 0):
        tempo[n] = tempo[n-1] + Ts
    toc[n] = t.time() - tic
conexao.write('0'.encode())
print('\nFim da coleta.')
conexao.close()

print('\nPeríodo real:', np.mean(toc))

#plt.figure(figsize=(10,6))
plt.plot(tempo,r,'-b',tempo,y,'-r',linewidth=1.2)
plt.xlabel('Tempo(s)')
plt.ylabel('Tensão (V)')
plt.grid()
plt.title('Onda Quadrada - Malha Aberta')
plt.legend(loc='lower right', labels=('Sinal de Entrada','Sinal de Saída'))
plt.show()