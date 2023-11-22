import matplotlib.pyplot as plt
import numpy as np
import pylab
s=input()
sym=list(s)
SYM=set(sym)
x=list(SYM)
print(x)
y=[]
n=0
for elem in x:
    n=sym.count(elem)
    y.append(n)
x1=np.array(x)
y1=np.array(y)
pylab.bar(x1,y1)
pylab.show()