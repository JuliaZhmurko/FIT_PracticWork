import math
class Circle4:
    def __init__(self,a1,b1):
        self.a=float(a1)
        self.b=float(b1)
   
    def radius_opus_rectangle(self):
        Ror=math.sqrt(pow(self.a,2)+pow(self.b,2))/2
        return(Ror)

    def radius_opus_square(self):
        Ros=self.a/math.sqrt(2)
        return(Ros)

    def radius_vpus_square(self):
        Rvs=self.a/2
        return(Rvs)

#a=float(input("Введіть сторону квадрата/ першу сторону прямокутника"))
#b=float(input("Введіть другу сторону прямокутника"))
#d = Circle4(a,b)
#print(d.radius_opus_rectangle())
#print(d.radius_opus_square())
#print(d.radius_vpus_square())
