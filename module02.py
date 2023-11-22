import math
Ax=float(input("x = "))
Ay=float(input("y = "))
Az=float(input("z = "))
Bx=float(input("x = "))
By=float(input("y = "))
Bz=float(input("z = "))
A=(Ax,Ay)
B=(Bx,By)
A1=(Ax,Ay,Az)
B1=(Bx,By,Bz)
print(A)
print(B)
print(A1)
print(B1)
def Vector_dobutok_plosh(r):
    return ((Ax*By)-(Ay*By)) #A*B
def Vector_dobutok_prost(r):
    return ((Ay*Bz)-(Az*By)-(Az*Bx)-(Ax*Bz)-(Ax*By)-(Ay*Bx)) #A1*B1
def Skal_dobutok_plosh(r):
    return (Ax*Bx)+(Ay*By) #A*B
def Skal_dobutok_prost(r):
    return (Ax*Bx)+(Ay*By)+(Az*Bz) #A1*B1
