import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

xn=[1,1,1,1]; print("xn=",xn)
N=4
Xk=DFT(xn,N); print("Xk=",Xk)
magXk=np.abs(Xk); print("Magnitude of Xk=",magXk)
phaXk=np.angle(Xk)*180/np.pi
print("Phase of Xk=",phaXk)
xn=np.real(IDFT(Xk,N)); print("Reconstructed xn=",xn)

