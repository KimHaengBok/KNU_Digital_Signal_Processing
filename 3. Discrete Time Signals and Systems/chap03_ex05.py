import numpy as np

n=np.arange(-2,5)  #순서시퀀스
N=len(n)  #시퀀스 길이
xn=np.zeros(N); xn[1]=1; xn[2]=1; xn[3]=0.5  #x(n)
hn=np.zeros(N); hn[2]=1; hn[3]=0.5; hn[4]=0.25  #h(n)
yn=np.zeros(N)  #y(n)

for i in range(N):
    if xn[i]!=0:  #x(n)의 값이 있으면
        print("n=",i)
        for k in range(3):
            yn[i+k]=yn[i+k]+xn[i]*hn[2+k]  #y(n)에 순서대로 더한다. 
        print("y(n)=",yn)


