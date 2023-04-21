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
from scipy.signal import max_len_seq, butter, lfilter

setpoint = 2.9
r = max_len_seq(10)[0]-0. + (setpoint)
numAmostras = len(r)
tempo = np.zeros(numAmostras)
y = np.zeros(numAmostras)
Ts = 0.015


toc = np.zeros(numAmostras)

    
print('\nEstabelecendo conexão.')
conexao = serial.Serial(port='COM3', baudrate=38400, timeout=0.005)
t.sleep(1)
print('\nIniciando coleta.')

for n in range(numAmostras):
    tic = t.time()

    if (conexao.inWaiting() > 0):
        y[n] = conexao.readline().decode()
           
    conexao.write(str(round(r[n]*255/5)).encode())
    
    t.sleep(0.015)
    
    if (n > 0):
        tempo[n] = tempo[n-1] + Ts
    toc[n] = t.time() - tic
conexao.write('0'.encode())
print('\nFim da coleta.')
conexao.close()

print('\nPeríodo real:', np.mean(toc))

np.savetxt("ensaio_0307.csv", [tempo, r, y], delimiter=",")

plt.figure(figsize=(10,8))
plt.subplot(211)
plt.plot(tempo,r,'-b', drawstyle="steps",lw=1.2)
plt.grid()
plt.title('Entrada PRBS')
plt.ylabel('Tensão (V)')
plt.subplot(212)
plt.plot(tempo, y,'-r', lw=1.2)
plt.grid()
plt.ylabel('Tensão (V)')
plt.xlabel('Tempo(s)')
plt.title('Sinal de Saída')
plt.show()