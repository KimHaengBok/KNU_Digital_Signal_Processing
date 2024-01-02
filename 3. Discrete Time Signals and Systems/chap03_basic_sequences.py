import numpy as np
import matplotlib.pylab as plt
from chap03_module import * 

n=[-3,-2,-1,0,1,2,3,4]    #순서시퀀스
xn=[2,1,-1,0,1,4,3,7]     #샘플시퀀스
plt.figure(1)     #1번 그림창 할당
plt.stem(n,xn,"blue"); plt.grid()     #그래프 그리기, 눈금 그리기
plt.xlabel("n"); plt.ylabel("x(n)")     #x축, y축 이름
plt.title("Representation of a sequence x(n)")     #그래프 제목

n0=0; n1=0; n2=20     #단위샘플위치:n0, 순서시퀀스 시작:n1, 끝:n2
N=n2-n1+1; n=np.arange(N)  #시퀀스길이,  #순서시퀀스
xn=impseq(n0,n1,n2); print("Unit sample sequence=",xn)     #단위샘플시퀀스생성
plt.figure(2)
plt.stem(n,xn,"blue"); plt.grid()     #그리기, 눈금그리기
plt.xlabel("n"); plt.ylabel("x(n)")     #x축, y축 이름
plt.title("Unit sample sequence")     #그래프 제목

n0=0; n1=0; n2=20     #단위계단시작위치:n0, 순서시퀀스 시작:n1, 끝:n2
N=n2-n1+1;  n=np.arange(N)  #시퀀스길이, #순서시퀀스
xn=stepseq(n0,n1,n2); print("Unit step sequence=",xn)     #단위계단시퀀스생성
plt.figure(3)
plt.stem(n,xn,"blue"); plt.grid()     #그리기, 눈금그리기
plt.xlabel("n"); plt.ylabel("x(n)")     #x축, y축 이름
plt.title("Unit step sequence")     #그래프 제목

a=0.7
N=20; n=np.arange(N)     #순서시퀀스
xn=np.power(a,n); print("Real-Valued exponential=",xn)  #실수지수 시퀀스
plt.figure(4)
plt.stem(n,xn,"blue"); plt.grid()     #그리기, 눈금그리기
plt.xlabel("n"); plt.ylabel("x(n)")     #x축, y축 이름
plt.title("Real-valued exponential sequence")     #그래프 제목

sigma=2; freq=3
n=np.linspace(0,10,100)     #순서시퀀스
xn=np.exp((sigma+freq*1j)*n)  #복소지수시퀀스 (amplitude)
magxn=abs(xn)    #절대값 복소지수시퀀스 (magnitude)
plt.figure(5)
plt.subplot(2,1,1); plt.stem(n,xn,"blue"); plt.grid()   #그리기, 눈금그리기
plt.ylabel("x(n), Amplitude")
plt.title("Complex-valued exponential sequence")
plt.subplot(2,1,2); plt.stem(n,magxn,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("|x(n)|, Magnitude")

n=np.linspace(0,10*np.pi,100)     #순서시퀀스, 0부터 10*pi까지 100등분, 0.1pi씩
xn=3*np.cos(0.1*np.pi*n+np.pi/2)  #정현파시퀀스
plt.figure(6)
plt.stem(n,xn,"blue"); plt.grid()   #그리기, 눈금그리기
plt.xlabel("n [samples]"); plt.ylabel("Amplitude")     #x축, y축 이름
plt.title("Sinusoidal sequence")     #그래프 제목

xn=np.random.rand(20); print("Random sequence x(n)=",xn)  #무작위샘플시퀀스
plt.figure(7)
n=np.arange(20)
plt.stem(n,xn,"blue"); plt.grid()   #그리기, 눈금그리기
plt.xlabel("n"); plt.ylabel("amplitude")     #x축, y축 이름
plt.title("Random sequence")     #그래프 제목

x=[1,2,3,4,5,6,7]; print("x=",x)   #샘플시퀀스
xn=5*x; print("xn=",xn)     #시퀀스 5회 복사
plt.figure(8)
n=np.arange(35)   #순서시퀀스
plt.stem(n,xn,"blue"); plt.grid()   #그리기, 눈금그리기
plt.xlabel("n"); plt.ylabel("amplitude")     #x축, y축 이름
plt.title("Peoriodic sequence")     #그래프 제목













