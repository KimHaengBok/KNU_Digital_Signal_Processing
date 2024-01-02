import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

xn=[0,1,2,3]; print("x(n)=",xn)     #이산주기신호의 기본주기구간
N=len(xn)     #이산주기신호의 주기
Xk=DTFS(xn,N); print("X(k)=",Xk); print("|X(k)|=",np.abs(Xk))    #DTFS 계수

n=np.arange(N)     #순서시퀀스 생성
plt.subplot(2,1,1); plt.stem(n,xn,"blue");plt.ylabel("x(n)")     #이산주기신호
plt.grid(); plt.title("DTFS of a discrete periodic signal x(n)")                
plt.subplot(2,1,2); plt.stem(n,np.abs(Xk),"green")    #DTFS 계수 
plt.xlabel("k"); plt.ylabel("|X(k)|"); plt.grid()                                   

