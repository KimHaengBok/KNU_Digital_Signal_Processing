import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from chap05_module import *

b=[1,0,-1]
a=[1,0,-0.81]
R,p,C=signal.residuez(b,a); print("R=",R); print("p=",p); print("C=",C)

b1=[1,1,0]
a1=[1,0,-0.81]
R1,p1,C1=signal.residuez(b1,a1); print("R1=",R1); print("p1=",p1);\
print("C1=",C1)

plt.figure(1); zplane(b,a)

Omega,H=signal.freqz(b,a,100)
magH=np.abs(H)
phaH=np.angle(H)
plt.figure(2)
plt.subplot(2,1,1); plt.plot(Omega,magH,"blue"); plt.grid()
plt.ylabel("magnitude"); plt.title("Magnitude & Phase Response")
plt.subplot(2,1,2); plt.plot(Omega,phaH,"blue"); plt.grid()
plt.xlabel("frequency in radian"); plt.ylabel("phase")



