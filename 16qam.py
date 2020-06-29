import matplotlib.pyplot as plt
import numpy as np
import math
plt.close('all')
Fs=2000
n=np.arange(0, 2, 1/Fs)
Fc=100
Ac=1
c = Ac*np.cos(2*math.pi*Fc*n)
Fm = 100
Am = 0.5
m = Am*np.sin(2*math.pi*Fm*n)
s = (1/2)*c+(1/2)*(c*np.cos(4*math.pi*Fc*n)+m*np.sin(4*math.pi*Fc*n))
plt.plot(n, s)
plt.title('sous modulation')
plt.xlabel('temp(s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
