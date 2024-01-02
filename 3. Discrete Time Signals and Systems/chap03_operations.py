import numpy as np
import matplotlib.pylab as plt
from chap03_module import *

n1=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x1=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
n2=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7])
x2=np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])

n,y,zx1,zx2=sigadd(n1,x1,n2,x2); print("y(n)=",y)
print("x1(n)=",zx1); print("x2(n)=",zx2); print("n=",n)
plt.figure(1)
plt.subplot(3,1,1); plt.stem(n,zx1,"blue"); plt.grid()
plt.ylabel("x1(zx1)"); plt.title("Signal Addition")
plt.subplot(3,1,2); plt.stem(n,zx2,"blue"); plt.grid(); plt.ylabel("x2(zx2)")
plt.subplot(3,1,3); plt.stem(n,y,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("y=x1+x2")

n,y,zx1,zx2=sigmult(n1,x1,n2,x2); print("y(n)=",y)
print("x1(n)=",zx1); print("x2(n)=",zx2); print("n=",n)
plt.figure(2)
plt.subplot(3,1,1); plt.stem(n,zx1,"blue"); plt.grid()
plt.ylabel("x1(zx1)"); plt.title("Signal Multiplication")
plt.subplot(3,1,2); plt.stem(n,zx2,"blue"); plt.grid(); plt.ylabel("x2(zx2)")
plt.subplot(3,1,3); plt.stem(n,y,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("y=zx1*zx2")

x1=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1]); print("x1(n)=",x1)
y=3*x1; print("y(n)=3x1(n)=",y)
plt.figure(3)
plt.subplot(2,1,1); plt.stem(n1,x1,"blue"); plt.grid(); plt.ylim(0,22)
plt.ylabel("x1(n)"); plt.title("Signal Scaling")
plt.subplot(2,1,2); plt.stem(n1,y,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("y(n)=3*x1(n)")

k=4
n,y=sigshift(n1,x1,k); print("n=",n);  print("y(n)=",y)
plt.figure(4)
plt.subplot(2,1,1); plt.stem(n1,x1,"blue"); plt.grid()
plt.ylabel("x1(n)"); plt.title("Signal Shifting")
plt.subplot(2,1,2); plt.stem(n,y,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("shift k=4, y(n)")

nx=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
ny,y=sigfold(nx,x);
print("nx=",nx); print("x=",x); print("ny=",ny); print("y=",y)
#결과를 그래프로 보기
n=np.arange(min(min(nx),min(ny)),max(max(nx),max(ny))+1) #순서시퀀스
N=int(max(max(nx),max(ny))-min(min(nx),min(ny))+1) #길이
zx=np.zeros(N); zx[int(min(nx)+abs(max(nx))):int(max(nx)+abs(max(nx))+1)]=x #삽입
zy=np.zeros(N); zy[int(min(ny)+abs(min(ny))):int(max(ny)+abs(min(ny))+1)]=y #삽입
plt.figure(5)
plt.subplot(2,1,1); plt.stem(n,zx,"blue"); plt.grid()
plt.ylabel("x(n)"); plt.title("Signal Folding")
plt.subplot(2,1,2); plt.stem(n,zy,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("y(n)=x(-n)")

n=np.array([-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
x=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
a1=-2; a2=7
y=np.sum(x[a1+abs(min(n)):a2+abs(min(n))+1])
print("n=",n); print("x=",x); print("y=",y)

n=np.array([-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
x=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
a1=-2; a2=7
y=np.prod(x[a1+abs(min(n)):a2+abs(min(n))+1])
print("n=",n); print("x=",x); print("y=",y)

x=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1]); print("x=",x)
y=np.sum(x*np.conjugate(x)); print("Energy of sequence x=",y)
y=np.sum(np.power(np.abs(x),2)); print("Energy of sequence x=",y)

x1=[1,2,3,5,4,6]
x=4*x1; print("periodic signal x=",x)
N=len(x); print("N=",N)
aa=np.sum(np.power(np.abs(x),2)); print("Energy of sequence x=",aa) 
y=1/N*aa; print("Power of sequence x=",y)


























