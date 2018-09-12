import numpy as np
import numpy.linalg as la

data = np.genfromtxt('datatraining.csv', delimiter=',')
cov_data=np.cov(np.transpose(data)) # Obtem matriz de covariancia dos dados
w,v=la.eig(cov_data)                # Obtem autovalores e autovetores

print(w)
print(v)