#############
# Problem 4 #
#############
import numpy as np
import matplotlib.pyplot as plt
from math import pi
f0, ax = plt.subplots(1,2,sharex=True, sharey=True)
f0.suptitle('Problem 4', fontsize = 'x-large')
N_k = 1001
for i, M in enumerate([10,50]):
    m = np.array(range((2*M+1)))-M
    k = np.linspace(-30,30,N_k)
    dx = 0.1
    m = m[:][np.newaxis]
    k = k[:][np.newaxis]
    matx = np.dot(m.T,k)*np.complex(0,1)
    ft_matx = dx*np.exp(2*pi*matx*dx)
    k = np.linspace(-30,30,N_k)
    sigma = np.sum(ft_matx,axis = 0)
    ax[i].plot(k,sigma.real, c= 'b')
    ax[i].hold(True)
    ax[i].plot(k,sigma.imag, c = 'r')
    ax[i].legend(['real','imag'])
    ax[i].set_title('M = %s' %M)
    ax[i].set_xlabel('k (1/cm)')
    ax[i].set_ylabel('Amplitude')
plt.show