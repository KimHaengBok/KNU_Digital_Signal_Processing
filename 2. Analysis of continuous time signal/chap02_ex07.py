import numpy as np
import matplotlib.pylab as plt

fs=5000; Ts=0.0002     #샘플링주파수와 샘플링주기
n=np.arange(-25,26)     #인덱스 어레이
xn=np.exp(-1000*np.abs(n*Ts))    #샘플신호(이산신호)
N=len(n)

dt=0.00005     #시간 간격
t=np.arange(-0.005,0.005,dt)     #sinc함수 시간축
Nt=len(t)     #sinc함수 시간축 길이

sinc_out=np.zeros(Nt)    #복원결과 출력배열
for i in range(Nt):    
    sum=0
    for j in range(N):     #각각의 n 위치마다, 싱크함수와의 곱의 합을 구한다.
        sum=sum+xn[j]*np.sinc(fs*(i*dt-j*Ts))
    sinc_out[i]=sum     #각각의 n 위치마다 출력배열에 저장한다.

plt.subplot(2,1,1); plt.stem(n,xn,"blue"); plt.ylabel("x(n)"); plt.grid()
plt.title("x(n), Reconstructed signal using sinc function")
plt.subplot(2,1,2); plt.plot(t,sinc_out,"red")
plt.xlabel("time in msec"); plt.ylabel("x(t)"); plt.grid()

