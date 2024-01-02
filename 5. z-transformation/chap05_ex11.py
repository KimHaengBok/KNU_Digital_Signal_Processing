import numpy as np
import matplotlib.pyplot as plt
from chap05_module import *

b=[1,0]
a=[1,-0.9]
plt.figure(1); zplane(b,a)

Omega,H=signal.freqz(b,a,100)
magH=np.abs(H)
phaH=np.angle(H)
plt.figure(2)
plt.subplot(2,1,1); plt.plot(Omega,magH,"blue"); plt.grid()
plt.ylabel("magnitude"); plt.title("Magnitude & Phase Response")
plt.subplot(2,1,2); plt.plot(Omega,phaH,"blue"); plt.grid()
plt.xlabel("frequency in radian"); plt.ylabel("phase")




