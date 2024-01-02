import numpy as np
from chap05_module import * 

b=[0,0,0,0.25,-0.5,0.0625]  #시스템함수의 분모 분자
a=[1,-1,0.75,-0.25,0.0625]
N=8
delta,n=impseq(0,0,7); print("impulse=",delta)
x=signal.lfilter(b,a,delta); print("x(n)=",x)  #X(z)로부터 x(n) 생성
n=np.arange(N)
s,n=stepseq(2,0,7); print("step u(n-2)=",s)
x=(n-2)*np.power(0.5,n-2)*np.cos(np.pi/3*(n-2))*s  #n에 대해 x(n) 생성
print("x(n)=",x)

