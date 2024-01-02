import numpy as np
import matplotlib.pylab as plt

n=np.arange(-10,11)
x=stepseq(0,-10,10)
n,xe,xo=evenodd(n,x)

plt.subplot(3,1,1); plt.stem(n,x,"blue")
plt.grid(); plt.ylabel("x(n)")
plt.title("Even-Odd decomposition of Sequence x(n)")
plt.subplot(3,1,2); plt.stem(n,xe,"blue")
plt.grid(); plt.ylabel("Even part xe(n)")
plt.subplot(3,1,3); plt.stem(n,xo,"blue")
plt.grid(); plt.xlabel("n"); plt.ylabel("Odd part xo(n)")

