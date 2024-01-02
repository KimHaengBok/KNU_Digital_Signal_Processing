import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from chap05_module import *

b=[0,1,1]
a=[1,-0.9,0.81]
plt.figure(1); zplane(b,a)

Omega,H=signal.freqz(b,a,100)
magH=np.abs(H)
phaH=np.angle(H)
plt.figure(2)
plt.subplot(2,1,1); plt.plot(Omega,magH,"blue"); plt.grid()
plt.ylabel("magnitude"); plt.title("Magnitude & Phase Response")
plt.subplot(2,1,2); plt.plot(Omega,phaH,"blue"); plt.grid()
plt.xlabel("frequency in radian"); plt.ylabel("phase")

R,p,C=signal.residuez(b,a); print("R=",R); print("p=",p); print("C=",C)
Mp=np.abs(p); print("Mp=",Mp)
Ap=np.angle(p)/np.pi; print("Ap=",Ap)


