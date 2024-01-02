import numpy as np
import matplotlib.pylab as plt
from scipy import signal
from chap03_module import *

b=[1]  #입력계수
a=[1,-1,0.9]  #출력계수

n=np.arange(100)  #순서시퀀스
xn1=impseq(0,0,99)  #단위임펄스 입력시퀀스
hn=signal.lfilter(b,a,xn1)  #임펄스응답시퀀스
plt.figure(1)
plt.subplot(2,1,1); plt.stem(n,xn1,"blue"); plt.grid(); plt.ylabel("x(n)")
plt.title("Impulse input x(n) and Impulse response h(n)")
plt.subplot(2,1,2); plt.stem(n,hn,"blue"); plt.grid(); plt.ylabel("h(n)")
plt.xlabel("n")

xn2=stepseq(0,0,99) #단위스텝 입력시퀀스
sn=signal.lfilter(b,a,xn2)  #단위스텝 응답시퀀스
plt.figure(2)
plt.subplot(2,1,1); plt.stem(n,xn2,"blue"); plt.grid(); plt.ylabel("x(n)")
plt.title("Unit step input x(n) and Unit step response s(n)")
plt.subplot(2,1,2); plt.stem(n,sn,"blue"); plt.grid(); plt.ylabel("s(n)")
plt.xlabel("n")

xn1_sum=np.sum(xn1); hn_sum=np.sum(hn)
sum1=hn_sum-xn1_sum; print("sum_of_unit impulse response=",sum1)
xn2_sum=np.sum(xn2); sn_sum=np.sum(sn)
sum2=sn_sum-xn2_sum; print("sum_of_unit step response=",sum2)


