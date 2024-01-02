import numpy as np
from chap03_module import *

xn=[3,11,7,0,-1,4,2]; n1=[-3,-2,-1,0,1,2,3] #x(n)과 순서시퀀스
hn=[2,3,0,-5,2,1]; n2=[-1,0,1,2,3,4]  #h(n)과 순서시퀀스
fn,fhn=sigfold(n2,hn)  #h(-n)과 순서시퀀스
print("x(n)=",xn," n1=",n1)
print("h(n)=",hn," n2=",n2)
print("h(-n)=",fhn," (-n2)=",fn)  

nmin=min(n1)+min(n2)  #컨볼루션 연산의 시작 순서
nmax=max(n1)+max(n2)  #컨볼루션 연산의 끝 순서  
n=np.arange(nmin,nmax+1)  #출력 y(n)의 순서시퀀스
N=len(n)  #출력 시퀀스의 길이
yn=np.zeros(N)  #출력 시퀀스 어레이 설정

for i in range(nmin,nmax+1):  #n의 시작부터 끝까지
    sum=0
    for j in range(int(min(fn)),int(max(fn)+1)):  #h(-n)의 시작부터 끝까지
        if ((i+j)>=min(n1) and (i+j)<=max(n1)):  #(n-k)가 x(n)의 순서 내이면
            sum=sum+xn[i+j+abs(min(n1))]*fhn[j+int(abs(min(fn)))]#컨볼루션 연산
    yn[i+abs(nmin)]=sum  #출력 처장

print("y(n)=",yn); print("n=",n)
    



