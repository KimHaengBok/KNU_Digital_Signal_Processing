import numpy as np
import matplotlib.pylab as plt
from scipy import signal
from chap08_module import *

OmegaS=[0.3*np.pi, 0.75*np.pi]    #디지털 저지대역주파수 [rad]
OmegaP=[0.4*np.pi, 0.6*np.pi]    #디지털 통과대역주파수 [rad]
Rp=1     #통과대역 리플 [dB]
As=40     #저지대역 감쇠 [dB]

OmegaS[0]=OmegaS[0]/np.pi; OmegaS[1]=OmegaS[1]/np.pi
OmegaP[0]=OmegaP[0]/np.pi; OmegaP[1]=OmegaP[1]/np.pi
print("\n","========== Digital Filtr Order/ Cutoff Frequency ===============")
N,OmegaC=signal.ellipord(OmegaP,OmegaS,Rp,As) #필터차수, 차단주파수
print("Filter order, N=",N)
print("Cutoff frequency, OmegaC=",OmegaC,"*pi")

print("\n","=========== Digital Filter System Function ======================")
b,a=signal.ellip(N,Rp,As,OmegaC,"bandpass") #시스템함수 분모/분자계수
print("Numerator coefficients=",b); print("Denominator coefficients=",a)

Omega,H=signal.freqz(b,a) #주파수축에서 주파수영역 크기응답 보기
plt.subplot(2,1,1); plt.plot(Omega/np.pi,abs(H),"blue")
plt.title("Frequency Response of Digital Elliptic Bandpass Filter")
plt.ylabel("|H|, Mgnitude"); plt.grid(); plt.xlim(0,1)

plt.subplot(2,1,2)
Frequency_response_Signal_filtering(b,a) #시간 축에서 신호필터링 결과 보기
