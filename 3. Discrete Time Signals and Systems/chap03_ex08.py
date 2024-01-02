import numpy as np
import matplotlib.pylab as plt
from chap03_module import *

nx=np.arange(-3,4)
nh=np.arange(-1,5)
xn=np.array([3,11,7,0,-1,4,2])
hn=np.array([2,3,0,-5,2,1])

n,y=convolve_m(nx,xn,nh,hn)
print("y(n)=x(n)*h(n)=",y); print("n=",n)

plt.subplot(3,1,1); plt.stem(nx,xn,"blue"); plt.grid()
plt.title("Convolution, y(n)=x(n)*h(n)"); plt.ylabel("x(n)"); plt.ylim(-2,12)
plt.subplot(3,1,2); plt.stem(nh,hn,"blue"); plt.grid()
plt.ylabel("h(n)"); plt.ylim(-6,5)
plt.subplot(3,1,3); plt.stem(n,y,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("y(n)")



