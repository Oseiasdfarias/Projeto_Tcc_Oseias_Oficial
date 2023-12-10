import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error

dados = pd.read_csv("ensaio_0407.csv", header=None).values

t_train, t_test = dados[0,0:500], dados[0,500:1001]
xtrain,  xtest  = dados[1,0:500], dados[1,500:1001]
ytrain,  ytest  = dados[2,0:500], dados[2,500:1001]

n = np.arange(3, len(xtrain))

M = np.array([ytrain[n-1], ytrain[n-2], xtrain[n-1], xtrain[n-2]]).T

x = np.linalg.inv(M.T@M)@M.T@ytrain[n]

#Validação

M_val = np.array([ytest[n-1], ytest[n-2], xtest[n-1], xtest[n-2]]).T

y_pred = M_val@x

# Erro médio quadrático
MSE = mean_squared_error(ytest[n], y_pred)
print('Erro médio quadrático: %.6f' % MSE)

# NRMSE:

def metricaNRMSE(yt,yp):
    return 1-np.sqrt(np.sum((yt-yp)**2))/np.sqrt(np.sum((yt-np.mean(yt))**2))

NRMSE = metricaNRMSE(ytest[n], y_pred)*100
print(NRMSE)

plt.subplot(211)
plt.plot(t_test, xtest, '-b', drawstyle='steps', linewidth=1.2)
plt.xlabel('tempo (s)')
plt.ylabel('Tensão (V)')
plt.title('Entrada PRBS')
plt.grid()

plt.subplot(212)
plt.plot(t_test[n], ytest[n], '-r', linewidth=1.2)
plt.plot(t_test[n], y_pred, '-g', linewidth=1.2)
plt.xlabel('tempo (s)')
plt.ylabel('Tensão (V)')
plt.title('Saída')
plt.legend(loc='lower right', labels=('Saída da planta', 'Saída do modelo'))
plt.grid()

plt.subplots_adjust(hspace=0.5)
plt.show()