import numpy as np
import matplotlib.pylab as plt
from scipy import signal
from chap08_module import *   #사용자정의함수파일

wp=0.2*np.pi; ws=0.3*np.pi; Rp=1; As=16     #설계 사양
N,wc=signal.cheb2ord(wp,ws,Rp,As,analog="true")   #필터차수, 정규화 차단주파수
print("필터차수 N=",N); print("차단주파수 wc=",wc,"=",wc/np.pi,"pi")

b,a=signal.cheby2(N,As,wc,"lowpass",analog="true")     #시스템함수 게수
print("시스템함수 Ha(s) 분자계수=",b); print("시스템함수 Ha(s) 분모계수=",a)

z,p,k=signal.cheby2(N,As,wc,"lowpass",analog="true",output="zpk")
print("영점",z); print("극점",p); print("이득=",k)

plt.figure(1)
zplane(b,a)     #극점-영점 다이어그램

b,a=signal.cheby2(N,As,wc/np.pi,"lowpass",analog=True) #차단주파수 정규화 [0~1]
w,H=signal.freqs(b,a) #정규화 주파수축[0~1], 주파수응답
plt.figure(2)
plt.plot(w,abs(H),"blue"); plt.grid(); plt.xlim(0,1)
plt.title("Magnitude Response of Chebyshev-2 Lowpass Filter")
plt.xlabel("frequency in pi radians")
plt.ylabel("|H|, Magnitude")

