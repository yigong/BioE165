#############
# Problem 2 #
#############
import numpy as np
import matplotlib.pyplot as plt
from math import pi
f0, ax = plt.subplots(1,2,sharex=True, sharey=True)
for i, N in enumerate([250,500]):
    x = np.linspace(0,4,N)
    y = np.cos(2*pi*x)
    y_analytic = -2*pi*np.sin(2*pi*x)
    der = [1,-1]
    y_num = np.convolve(y,der,mode='same')
    ax[i].plot(x,y_analytic, linestyle = '-.')
    ax[i].hold(True)
    ax[i].plot(x,y_num*N/4, c = 'r', linestyle = ':')
    ax[i].legend(['Analytical derivative','Numerical derivative'])
    ax[i].set_title('N = %s' %str(N))
    ax[i].set_ylim(-20,20)
f0.suptitle('Problem 2', fontsize = 'x-large')
plt.show()