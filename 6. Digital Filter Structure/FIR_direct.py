import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def FIR_direct(x):     #직접형 FIR 필터
    y=[0]*tn
    for n in range(4, len(x)):
        y[n]=x[n]+16.0625*x[n-4]+x[n-8]
    return y

tn=5000     #총 데이터 샘플 수
t = np.linspace(0, 1, tn)     #x축 설정
input = chirp(t, f0=10, t1=0.2, f1=500, method='linear')     #처퍼신호 발생
Filter_output=[0]*tn     #필터 출력 어레이 설정
Filter_output=FIR_direct(input)    #필터 출력 계산 

plt.plot(Filter_output,"b"); plt.xlim(0,5000)
plt.xlabel("samples, frequncy[0~500Hz]"); plt.grid()
plt.title("Frequency filtering result of FIR direct filter")

