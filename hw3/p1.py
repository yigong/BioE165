import numpy as np
import matplotlib.pyplot as plt
ctable= ['b','r']
lstyle = ['-.',':']
f0, [ax0,ax1,ax2] = plt.subplots(1,3)
f0.suptitle('Problem 1',fontsize = 'x-large')
ax0.set_title('A*rect(x/a)')
ax1.set_title('B*rect(x/b)')
ax2.set_title('convoluted signal')
for i, N in enumerate([250,500]):
    A = 1.
    B = 1.
    a = 4.
    b = 1.
    x1 = np.linspace(-10,10,N)
    x2 = np.linspace(-10,10,N)
    y1 = np.where((x1>-a/2) & (x1<=a/2), A*1., 0.)
    y2 = np.where((x2>-b/2) & (x2<=b/2), B*1., 0.)
    #y1 = y1/y1.sum()
    y2_scaled = y2/y2.sum()
    trapz = np.convolve(y1,y2_scaled,mode='same')
    ax0.hold(True)
    ax0.plot(x1,y1, color = ctable[i], linestyle = lstyle[i])
    ax0.set_xlim(-3,3)
    ax1.plot(x2,y2, color = ctable[i], linestyle = lstyle[i])
    ax1.set_xlim(-3,3)
    ax2.plot(x1,trapz, color = ctable[i], linestyle = lstyle[i])
    ax2.set_xlim(-3,3)
    ax2.legend(('N = 250','N = 500'),loc = 'lower right')
plt.show()
