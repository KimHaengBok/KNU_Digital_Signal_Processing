import numpy as np
import matplotlib.pylab as plt
from scipy.signal import chirp
from chap08_module import *  

Omegap=0.2*np.pi    #디지털 통과대역주파수 [rad]
Omegas=0.3*np.pi    #디지털 저지대역주파수 [rad]
Rp=1; As=15   #통과대역 리플과 저지대역 감쇄 [dB]
T=1; Fs=1/T     #샘플구간과 샘플주파수
wp=2/T*np.tan(Omegap/2); print("wp=",wp) #아날로그 통과대역 에지주파수 사전래핑
ws=2/T*np.tan(Omegas/2); print("ws=",ws) #아날로그 저지대역 에지주파수 사전래핑

print("\n","============= Filter order, Cutoff frequency ===================")
N,wc=signal.ellipord(wp,ws,Rp,As,analog=True)     #필터차수, 차단주파수
print("Filter order N=",N)
print("Cutoff frequency, wc=",wc,"=",wc/np.pi,"*pi")
print("\n","============= Analog Filter ====================================")
c,d=signal.ellip(N,Rp,As,wc,"lowpass",analog=True) #아날로그 시스템함수 계수
print("Numerator coefficients=",c); print("Denomunator coefficients=",d)
print("\n","========== Digital Filter(Direct Type) =========================")
b,a=signal.bilinear(c,d,Fs)     #이선형변환(s->z), 디지털 시스템함수 계수
print("Numerator coefficients=",b); print("Denomunator coefficients=",a)

plt.figure(1)
Omega,H=signal.freqz(b,a)  #주파수축, 주파수응답
plt.plot(Omega/np.pi,abs(H),"blue"); plt.xlabel("Frequency in pi radians")
plt.title("Frequency Response of Digital Elliptic Lowpass Filter")
plt.ylabel("|H|, Magnitude"); plt.grid(); plt.xlim(0,1)

plt.figure(2)
Frequency_response_Signal_filtering(b,a)

