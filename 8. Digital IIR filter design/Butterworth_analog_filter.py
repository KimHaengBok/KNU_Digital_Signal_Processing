import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from chap08_module import *


wp=0.2*np.pi; ws=0.3*np.pi; Rp=7; As=16 #설계 사양
N,wc=signal.buttord(wp,ws,Rp,As,analog=True)
print("필터차수 N=",N); print("차단주파수 wc=",wc,"=",wc/np.pi,"pi")

b,a=signal.butter(N,wc,"lowpass",analog=True)
print("시스템함수 Ha(s) 분자계수=",b); print("시스템함수 Ha(s) 분모계수=",a)

z,p,k=signal.butter(N,wc,"lowpass",analog=True,output="zpk")
print("영점",z); print("극점",p); print("이득=",k)

plt.figure(1)
zplane(b,a) #극점-영점 다이어그램

b,a=signal.butter(N,wc/np.pi,"lowpass",analog=True) #차단주파수 정규화 [0~1]
w,H=signal.freqs(b,a) #정규화 주파수축[0~1], 주파수응답
plt.figure(2)
plt.plot(w,abs(H),"blue"); plt.grid(); plt.xlim(0,1) #크기응답
plt.title("Magnitude response of Butterworth Lowpass Filter")
plt.xlabel("Frequency in pi radians")
plt.ylabel("|H|, Magnitude")



