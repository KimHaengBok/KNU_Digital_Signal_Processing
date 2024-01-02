import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import chirp
from chap07_module import *
 
Omega_p=0.7*np.pi; Omega_s=0.6*np.pi     #통과대역에지주파수, 저지대역에지주파수
tr_width=Omega_p-Omega_s     #천이대역폭
M=int(np.ceil(6.2*np.pi/tr_width)); print("M=",M)     #창 길이
Omega_c=(Omega_s+Omega_p)/2     #차단주파수
nt=np.arange(0,M)     #시퀀스 축

hd=ideal_lp(np.pi,M)-ideal_lp(Omega_c,M)     #이상적인 HPF 임펄스응답
wn=signal.hann(M)     #핸 창 함수
hn=hd*wn     #유한 임펄스응답

nf,H=signal.freqz(hn)     #주파수축, 주파수응답
H_dB=20*np.log10(abs(H))     #주파수응답(dB)

plt.subplot(3,1,1); plt.stem(nt,hn,"b"); plt.grid()
plt.ylabel("h(n)"); plt.xlabel("n"); plt.xlim(0,M-1)
plt.title("Impulse response, Frequency response, Frequency filtering result")

plt.subplot(3,1,2); plt.plot(nf/np.pi,H_dB,"b"); plt.grid(); plt.xlim(0,1)
plt.xlabel("Frequency in pi radians"); plt.ylabel("Magnitude [dB]")

t=np.linspace(0,1,5000)
xn=chirp(t,f0=10, t1=0.2, f1=500, method="linear") #처프신호 생성
yn=np.convolve(hn,xn) #컨볼루션으로 출력생성
plt.subplot(3,1,3); plt.plot(yn,"b"); plt.xlim(0,5000)
plt.xlabel("Samples(Frequency(0~500[Hz]))"); plt.grid()

