import numpy as np

data = np.genfromtxt('datatraining.csv', delimiter=',')
np.cov(np.transpose(data))
