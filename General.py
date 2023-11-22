import General_Calc as clm

while True:
    try:
        A = x, y, z = [float(s) for s in input('вкажіть координати точки А через "пробіл" x y z >>: ').split()]
    except ValueError:
        print('вкажіть корректне значення кординат точки А!')
    else:
        break
while True:
    try:
        B = x, y, z = [float(s) for s in input('вкажіть координати точки В через "пробіл" x y z >>: ').split()]
    except ValueError:
        print('вкажіть корректне значення кординат точки В!')
    else:
        break

#Ax, Ay, Az, Bx, By, Bz
my_Cord = A+B
print(my_Cord)

print("Vector_dobutok_plosh = ", clm.Vector_dobutok_plosh(*my_Cord))
print("Vector_dobutok_prost = ", clm.Vector_dobutok_prost(*my_Cord))
print("Skal_dobutok_plosh = ", clm.Skal_dobutok_plosh(*my_Cord))
print("Skal_dobutok_prost = ", clm.Skal_dobutok_prost(*my_Cord))