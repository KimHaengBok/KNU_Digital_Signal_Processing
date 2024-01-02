import numpy as np
import matplotlib.pyplot as plt
from chap07_module import *     #사용자정의함수 사용

hn=np.array([-4,1,-1,-2,5,6,-6,-5,2,1,-1,4])    #임펄스응답
M=12; n=np.arange(0,M)     #필터길이, 시퀀스축
Omega=np.linspace(0, np.pi, 1000)     #0에서 3.14까지 1000등분

H=np.arange(1000); H=np.float64(H)     #주파수응답
for x in range(1000):
    H[x]=2*hn[5]*np.sin(Omega[x]*(1-1/2))+2*hn[4]*np.sin(Omega[x]*(2-1/2))\
    +2*hn[3]*np.sin(Omega[x]*(3-1/2))+2*hn[2]*np.sin(Omega[x]*(4-1/2))\
    +2*hn[1]*np.sin(Omega[x]*(5-1/2))+2*hn[0]*np.sin(Omega[x]*(6-1/2))
amplitude=H     #진폭응답
magnitude=abs(H)     #크기응답
phase=np.angle(H)*180/np.pi    #위상응답

plt.figure(1)
plt.subplot(2,2,1); plt.stem(n,hn,"b"); plt.grid()
plt.title("Impulse Response")
plt.subplot(2,2,2); plt.plot(Omega/np.pi,magnitude,"g"); plt.grid()
plt.ylabel("Magnitude"); plt.title("Magnitude Response")
plt.subplot(2,2,4); plt.plot(Omega/np.pi,phase,"b"); plt.grid()
plt.ylabel("Phase"); plt.xlabel("Frequency in pi radians")
plt.title("Phase Response")
plt.figure(2)
plt.subplot(2,2,2); an=np.array([1,0]); zplane(hn,an); plt.grid()
plt.title("Pole-Zero Diagram")

