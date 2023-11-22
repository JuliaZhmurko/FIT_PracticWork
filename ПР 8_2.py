import numpy as np
from array import*

mas = np.array([[63, 25],[40, 15]])
print(mas)
A=mas[0]
B=mas[1]
det = A[0]*B[-1]-A[-1]*B[0]
print("Визначник матриці 2-го порядку = {0}".format(det))
print("----")
print("Перетворюємо масив 2х2 в одновимірний 1х4:")
mas_n = array('i',A)
mas_n.extend(B)
print(mas_n)