import Circle4 as cl
a=float(input('Введіть сторону квадрата/ першу сторону прямокутника>>:'))
b=float(input("Введіть другу сторону прямокутника>>:"))
d = cl.Circle4(a,b)
print("Радіус кола описаного навколо прямокутника>>:",d.radius_opus_rectangle())
print("Радіус кола описаного навколо квадрата>>:",d.radius_opus_square())
print("Радіус кола вписаного в квадрат>>:",d.radius_vpus_square())

    