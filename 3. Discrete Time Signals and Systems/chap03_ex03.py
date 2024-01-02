import numpy as np
import matplotlib.pylab as plt

n=np.arange(-10,11)
alpha=-0.1+0.3*1j
x=np.exp(alpha*n)

plt.subplot(4,1,1); plt.stem(n,np.real(x),"blue")
plt.grid(); plt.ylabel("Real part")
plt.title("Four parts of sequence x(n)")
plt.subplot(4,1,2); plt.stem(n,np.imag(x),"blue")
plt.grid(); plt.ylabel("Imaginary part")
plt.subplot(4,1,3); plt.stem(n,np.abs(x),"blue")
plt.grid(); plt.ylabel("Magnitude part")
plt.subplot(4,1,4); plt.stem(n,np.angle(x)*180/np.pi,"blue")
plt.grid(); plt.ylabel("Phase part"); plt.xlabel("n")

