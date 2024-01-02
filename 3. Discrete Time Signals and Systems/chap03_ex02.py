import numpy as np
import matplotlib.pylab as plt
from chap03_module import * 

n=np.arange(-2,11)
x=np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])

n11,x11=sigshift(n,x,5); print(n11,x11)
n12,x12=sigshift(n,x,-4); print(n12,x12)

n1,x1,y1,y2=sigadd(n11,2*x11,n12,-3*x12)
plt.subplot(2,1,1); plt.stem(n1,x1,"blue"); plt.grid(); plt.ylabel("x1(n)")
plt.title("Sequences of Example 3-2, a, b")

n21,x21=sigfold(n,x)
n21,x21=sigshift(n21,x21,3)
n22,x22=sigshift(n,x,-4)
n22,x22,y1,y2=sigmult(n,x,n22,x22)

n2,x2,y1,y2=sigadd(n21,x21,n22,x22)
plt.subplot(2,1,2); plt.stem(n2,x2,"blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x2(n)")

