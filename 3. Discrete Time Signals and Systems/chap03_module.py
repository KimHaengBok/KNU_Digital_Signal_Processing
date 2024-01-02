import numpy as np

def impseq(n0,n1,n2):     #단위샘플시퀀스
    N=n2-n1+1     #데이터수
    n=np.arange(N)     #순서시퀀스
    xn=np.zeros(N)     #데이터어레이 설정
    for i in range(N):     #단위샘플시퀀스 생성
        if (i+n1)==n0: xn[i]=1
    return xn     #리턴

def stepseq(n0,n1,n2):     #단위계단시퀀스
    N=n2-n1+1     #데이터수
    n=np.arange(N)     #순서시퀀스
    xn=np.zeros(N)     #데이터어레이 설정
    for i in range(N):     #단위계단시퀀스 생성
        if (i+n1)>=n0: xn[i]=1
    return xn     #리턴

def sigadd(n1,x1,n2,x2):   #신호덧셈
    nk=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)   #전체 시퀀스축
    N=len(nk)   #전체 시퀀스길이
    y1=np.zeros(N)   #x1 영점자리맞춤 배열생성
    y2=np.zeros(N)   #x2 영점자리맞춤 배열생성
    aa=abs(min(min(n1),min(n2)))     #자리맞춤이동폭
    n1=n1+aa     #자리이동
    n2=n2+aa     #자리이동
    y1[int(min(n1)):int(max(n1)+1)]=x1     #샘플저장
    y2[int(min(n2)):int(max(n2)+1)]=x2     #샘플저장
    y=y1+y2   #샘플대샘플 덧셈
    return nk,y,y1,y2
    
def sigmult(n1,x1,n2,x2):    #신호곱셈
    n=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)   #전체 시퀀스축
    N=len(n)   #전체 시퀀스길이
    y1=np.zeros(N)   #x1 영점자리맞춤 배열생성
    y2=np.zeros(N)   #x2 영점자리맞춤 배열생성
    aa=abs(min(min(n1),max(n1),min(n2),max(n2))); #배열자리이동
    y1[min(n1)+aa:max(n1)+aa+1]=x1
    y2[min(n2)+aa:max(n2)+aa+1]=x2
    y=y1.T*y2   #샘플대샘플 곱셈
    return n,y,y1,y2

def sigshift(m,x,k):     #신호이동
    n=m+k   #시퀀스축 이동
    y=x    #신호복사
    return n,y

def sigfold(n1,x1):    #신호반전
    N=len(n1)    #신호길이
    y=np.zeros(N)     #출력어레이 설정
    n=np.zeros(N)
    for i in range(N):     #샘플교환
        y[i]=x1[N-1-i]
        n[i]=-1*n1[N-1-i]
    return n,y

def evenodd(n,x):    #x(n)의 기수, 우수 찾기
    n1,xa=sigfold(n,x)   #x(n)의 폴딩 시퀀스
    n,xe,y1,y2=sigadd(n,x,n1,xa)
    n,xo,y1,y2=sigadd(n,x,n1,-xa)
    xe=xe/2     #기수계산
    xo=xo/2     #우수계산
    return n,xe,xo
    
def convolve_m(nx,x,nh,h):  #두 시퀀스의 컨볼루션
    nyb=nx[0]+nh[0]   #계산 k 시작점
    nye=nx[len(x)-1]+nh[len(h)-1]    #계산 k 종점    
    ny=np.arange(nyb,nye+1)   #순서시퀀스 할당
    y=np.convolve(x,h)    #컨볼루션 출력
    return ny,y


    
    
    
    
    





























