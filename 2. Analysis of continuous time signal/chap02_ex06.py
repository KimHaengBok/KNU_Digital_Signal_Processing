import numpy as np
import matplotlib.pylab as plt

w=np.arange(-2*np.pi,2*np.pi,0.1)    #주파수축 설정
N=len(w)     #전체 주파수축 길이
Xw=np.zeros(N)    #CTFT 결과 계수 저장 어레이
T=1    #주기를 1로 둔다.
for i in range(-int(N/2),int(N/2)):
    if i==0:
        Xw[i+int(N/2)]=1     #싱크함수 f=0에서의 조건
    if i!=0:
        Xw[i+int(N/2)]=np.sin(i*T/2)/(i/2)    #CTFT 계수 X(f) 계산

plt.plot(w,Xw,"blue")
plt.stem(w,Xw,"blue"); plt.grid()
plt.xlabel("w, frequency in radians"); plt.ylabel("X(w)")
plt.title("CTFT, of a non-periodic signal")



