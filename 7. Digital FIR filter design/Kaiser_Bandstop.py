import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import chirp
from chap07_module import * 
   
M=45     #창 길이 결정
As=50     #저지대역 감쇠
beta=0.1102*(As-8.7)     #베타 값 계산
nt=np.arange(0,M)     #시퀀스 축

Omega_c1=np.pi/3; Omega_c2=np.pi*2/3   #하위 및 상위 차단주파수
hd=ideal_lp(Omega_c1,M)+(ideal_lp(np.pi,M)-ideal_lp(Omega_c2,M))  #임펄스응답
wn=signal.kaiser(M,beta)     #카이저 창 함수
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
yn=np.convolve(hn,xn) #컨볼루션
plt.subplot(3,1,3); plt.plot(yn,"b"); plt.xlim(0,5000)
plt.xlabel("Samples(Frequency(0~500[Hz]))"); plt.grid()

