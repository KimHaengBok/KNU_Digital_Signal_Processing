import numpy as np
import matplotlib.pylab as plt
from scipy import signal
from chap03_module import *

b=[1]  #입력계수
a=[1,-0.9]  #출력계수
n=np.arange(0,51)  #순서시퀀스
xn=stepseq(0,0,50)-stepseq(10,0,50)  #입력시퀀스
hn=np.power(0.9,n)  #임펄스응답시퀀스
yn=signal.lfilter(b,a,xn)  #출력시퀀스

plt.subplot(3,1,1); plt.stem(n,xn,"blue"); plt.grid(); plt.ylabel("x(n)")
plt.title("Input x(n), Impulse response h(n) and Output y(n)")
plt.subplot(3,1,2); plt.stem(n,hn,"blue"); plt.grid(); plt.ylabel("h(n)")
plt.subplot(3,1,3); plt.stem(n,yn,"blue"); plt.grid(); plt.ylabel("y(n)")
plt.xlabel("n")



