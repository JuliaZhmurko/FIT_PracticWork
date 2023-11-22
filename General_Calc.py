import math

def Vector_dobutok_plosh(Ax, Ay, Az, Bx, By, Bz):
    return ((Ax*By)-(Ay*By)) #A*B

def Vector_dobutok_prost(Ax, Ay, Az, Bx, By, Bz):
    return ((Ay*Bz)-(Az*By)-(Az*Bx)-(Ax*Bz)-(Ax*By)-(Ay*Bx)) #A1*B1

def Skal_dobutok_plosh(Ax, Ay, Az, Bx, By, Bz):
    return (Ax*Bx)+(Ay*By) #A*B

def Skal_dobutok_prost(Ax, Ay, Az, Bx, By, Bz):
    return (Ax*Bx)+(Ay*By)+(Az*Bz) #A1*B1