import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def IIR_cascade(x):     #직렬형 IIR 필터
    y=[0]*tn
    v=[0]*tn
    for n in range(4, len(x)):
        v[n]=x[n]-v[n-1]+(9*x[n-2]-0.5*v[n-2])
        y[n]=1/16*(v[n]+(-3*v[n-1]+0.25*y[n-1])+(2*v[n-2]+0.125*y[n-2]))
    return y

tn=5000     #총 데이터 샘플 수
t = np.linspace(0, 1, tn)     #x축 설정
input = chirp(t, f0=10, t1=0.2, f1=500, method='linear')     #처퍼신호 발생
IIR_cascade_output=[0]*tn     #필터 출력 어레이 설정
IIR_cascade_output=IIR_cascade(input)  #필터 출력 계산

plt.plot(IIR_cascade_output,"b"); plt.xlim(0,5000)
plt.xlabel("samples, frequncy[0~500Hz]"); plt.grid()
plt.title("Frequency filtering result of IIR Cascade filter")

