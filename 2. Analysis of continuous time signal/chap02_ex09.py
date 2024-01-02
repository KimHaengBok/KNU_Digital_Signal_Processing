import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import *

Ts=0.0002     #샘플링 주기
n=np.arange(-25,26)     #순서시퀀스 어레이
xn=np.exp(-1000*np.abs(n*Ts))     #샘플시퀀스
ft=interp1d(n,xn,kind="linear")    #일차보간 적용
tn=np.linspace(-25,25,1000)  #보간할 미세구간 설정 

plt.subplot(2,1,1); plt.stem(n,xn,"blue"); plt.ylabel("x(n)"); plt.grid()
plt.title("Signal reconstruction using first-order interpolation")
plt.subplot(2,1,2); plt.plot(tn,ft(tn),"red"); plt.grid()
plt.xlabel("tn"); plt.ylabel("xa(t)")
plt.stem(n,xn,"blue",".")  #덧그리기

