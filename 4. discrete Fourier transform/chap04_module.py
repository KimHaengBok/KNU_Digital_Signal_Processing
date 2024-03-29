import numpy as np

def DTFS(xn,N):     #이산주기신호와 주기로부터 DTFS 계수 구하는 함수
    WN=np.exp(-1j*(2*np.pi/N))     #복소지수항
    Xk=np.zeros(N, dtype="complex64")     #DTFS 계수 어레이 설정
    for i in range(N):
        sum=0
        for j in range(N):
            sum=sum+xn[j]*np.power(WN,i*j)     #개별 DTFS 계수 계산
        Xk[i]=sum
    return Xk     #DTFS 계수값 리턴

def IDTFS(Xk,N):     #DFS 계수 X(k)와 길이 N으로부터 시퀀스 x(n) 구하는 역 DFS
    WN=np.exp(-1j*(2*np.pi/N))     #복소수 지수항
    xn=np.zeros(N, dtype="complex64")     #DFS 계수, 복소수
    for i in range(N):
        sum=0
        for j in range(N):
            sum=sum+Xk[j]*np.power(WN,-i*j)     #개별 역 DFS 계산
        xn[i]=sum/N
    return xn     #역 DFS 시퀀스 리턴

def DFT(xn,N):     #이산푸리에변환
    WN=np.exp(-1j*(2*np.pi/N))     #회전인자 게산
    Xk=np.zeros(N, dtype="complex64")     #DFT 계수 어레이 설정
    for i in range(N):
        sum=0
        for j in range(N):
            sum=sum+xn[j]*np.power(WN,i*j)     #DFT 계수 계산
        Xk[i]=sum
    return Xk     #DFT 계수 리턴

def IDFT(Xk,N):     #역 이산푸리에변환
    WN=np.exp(-1j*(2*np.pi/N))     #회전인자 게산
    xn=np.zeros(N, dtype="complex64")     #복원 이산신호 어레이 설정
    for i in range(N):
        sum=0
        for j in range(N):
            sum=sum+Xk[j]*np.power(WN,-i*j)     #역 DFT 계산
        xn[i]=sum/N
    return xn     #IDFT 계수 리턴

def DTFT(xn,N,T):     #이산시간푸리에변환
    w=np.linspace(0,2*np.pi,T)    #주파수축 
    MXe=np.zeros(T, dtype="complex64")     #DTFT 계수, 복소수
    for i in range(T):
        sum=0    #DTFT 계수 계산
        MXe[i]=np.sin(2*w[i])/np.sin(w[i]/2)*np.exp(-1j*w[i]*3/2)
    return MXe     #DTFT 계수 리턴










