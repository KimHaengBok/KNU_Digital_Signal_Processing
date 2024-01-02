import numpy as np
import matplotlib.pylab as plt
from chap04_module import * 

N=10
xn=np.zeros(N,dtype="float")
for i in range(N):
    xn[i]=np.cos(0.48*np.pi*i)+np.cos(0.52*np.pi*i)
print("x(n)=",xn); print()
Xk=DFT(xn,N)
magXk=np.abs(Xk); print("Magnitude of X(k)=",magXk)

n=np.arange(N)
fn=np.linspace(0,np.pi,int(N/2)+1); print("fn=",fn)
plt.figure(1)
plt.subplot(2,1,1); plt.stem(n,xn,"blue")
plt.grid(); plt.ylabel("x(n)")
plt.title("Sequence x(n) and DFT X(k), N=10")
plt.subplot(2,1,2); plt.stem(fn,magXk[0:int(N/2)+1],"green")
plt.grid(); plt.ylabel("|X(k)|"); plt.xlabel("frequency in radian")

N1=100
xn1=np.zeros(N1,dtype="float")
xn1[0:N]=xn
Xk1=DFT(xn1,N1)
magXk1=np.abs(Xk1)

n1=np.arange(N1)
fn=np.linspace(0,np.pi,int(N1/2)+1)
plt.figure(2)
plt.subplot(2,1,1); plt.stem(n1,xn1,"blue")
plt.grid(); plt.ylabel("x(n)")
plt.title("Sequence x(n) and DFT X(k), N=100, 90 zero-padding")
plt.subplot(2,1,2); plt.stem(fn,magXk1[0:int(N1/2)+1],"green")
plt.grid(); plt.ylabel("|X(k)|"); plt.xlabel("frequency in radian")

N2=100
xn=np.arange(N2,dtype="float")
for i in range(N2):
    xn[i]=np.cos(0.48*np.pi*i)+np.cos(0.52*np.pi*i)
Xk2=DFT(xn,N2); len(Xk2)
magXk2=np.abs(Xk2); print("|X(k)|=",magXk2)

n2=np.arange(N2)
fn=np.linspace(0,np.pi,int(N2/2)+1)
plt.figure(3)
plt.subplot(2,1,1); plt.stem(n2,xn,"blue")
plt.grid(); plt.ylabel("x(n)")
plt.title("Sequence x(n) and DFT X(k), N=100, no zero-padding")
plt.subplot(2,1,2); plt.stem(fn,magXk2[0:int(N2/2)+1],"green")
plt.grid(); plt.ylabel("|X(k)|"); plt.xlabel("frequency in radian")


