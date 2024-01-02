import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def IIR_parallel(x):     #병렬형 IIR 필터
    y=[0]*tn
    v1=[0]*tn
    v2=[0]*tn
    for n in range(4, len(x)):
        v1[n]=-10.05*x[n]-3.95*x[n-1]-v1[n-1]-0.5*v1[n-2]
        v2[n]=28.1125*x[n]-13.3625*x[n-1]+0.25*v2[n-1]+0.125*v2[n-2]
        y[n]=-18*x[n]+v1[n]+v2[n]
    return y

tn=5000     #총 데이터 샘플 수
t = np.linspace(0, 1, tn)     #x축 설정
input = chirp(t, f0=10, t1=0.2, f1=500, method='linear')     #처퍼신호 발생
IIR_parallel_output=[0]*tn     #필터 출력 어레이 설정
IIR_parallel_output=IIR_parallel(input)  #필터 출력 계산

plt.plot(IIR_parallel_output,"b"); plt.xlim(0,5000)
plt.xlabel("samples, frequncy[0~500Hz]"); plt.ylim(-8,8); plt.grid()
plt.title("Frequency filtering result of IIR Parallel filter")

