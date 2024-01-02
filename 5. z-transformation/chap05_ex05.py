import numpy as np
from chap05_module import * 

x1=[1,2,3]; n1=np.arange(-1,2)
print("x1(n)=",x1,"n1=",n1)
x2=[2,4,3,5]; n2=np.arange(-2,2)
print("x2(n)=",x2,"n2=",n2)
x3,n3=convolve_m(x1,n1,x2,n2)
print("x3(n)=",x3,"n3=",n3)

