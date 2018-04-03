import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('monas.txt')
time = range(0, len(datos[:,0]))
numero = datos[:,0]
rep = datos[:,1]

plt.figure()
plt.plot(time, numero, label = ' numero de laminas')
plt.plot(time, rep, label = 'laminas repetidas')
plt.legend()
plt.savefig('album.pdf')

