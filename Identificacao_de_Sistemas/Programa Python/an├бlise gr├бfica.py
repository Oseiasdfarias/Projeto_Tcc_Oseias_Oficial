# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:51:52 2020

@author: FelipePiano
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import control as ct
from sklearn.metrics import mean_squared_error

dados = pd.read_csv('ensaio.csv',header=None).values

tempo = dados[0,200:]
entrada = dados[1,200:]
saida = dados[2,200:]

r = entrada - 1.25
y = saida - 1.09

#Função de tranferência
a = 8.3333; K = 11.83
sys = ct.TransferFunction([K],[1,a])
y_ft = ct.forced_response(sys,T=tempo,U=r)[1]

#plt.figure(figsize=(10,6))
plt.plot(tempo,y_ft,'-b',linewidth=1.2)
plt.plot(tempo,y,'-r',linewidth=1.2)
plt.plot(tempo,r,'-k',linewidth=1.4)
plt.xlabel('Tempo(s)')
plt.ylabel('Tensão (V)')
plt.title('Onda Quadrada - Malha Aberta')
plt.legend(loc='upper right', labels=('Modelo Linear','Sinal de Saída',
                                      'Sinal de Entrada'))
plt.grid(True)
plt.show()
eqm = mean_squared_error(y,y_ft)
print(eqm)
