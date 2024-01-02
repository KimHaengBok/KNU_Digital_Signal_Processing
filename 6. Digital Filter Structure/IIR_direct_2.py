import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

def IIR_direct_2(x):     #제2 직접형 IIR 필터
    y=[0]*tn
    v=[0]*tn
    for n in range(4, len(x)):
        v[n]=x[n]-12/16*v[n-1]-2/16*v[n-2]+4/16*v[n-3]+1/16*v[n-4]
        y[n]=1/16*v[n]-3/16*v[n-1]+11/16*v[n-2]-27/16*v[n-3]+18/16*v[n-4]
    return y

tn=5000     #총 데이터 샘플 수
t = np.linspace(0, 1, tn)     #x축 설정
input = chirp(t, f0=10, t1=0.2, f1=500, method='linear')     #처퍼신호 발생
IIR_direct_2_output=[0]*tn     #필터 출력 어레이 설정
IIR_direct_2_output=IIR_direct_2(input)    #필터 출력 계산 

plt.plot(IIR_direct_2_output,"b"); plt.xlim(0,5000)
plt.xlabel("samples, frequncy[0~500Hz]"); plt.grid()
plt.title("Frequency filtering result of IIR Direct-2 filter")

