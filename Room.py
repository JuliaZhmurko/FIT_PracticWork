class Room:
    square='18'
    color='brown'
    def __init__(self,square1,color1):
        self.color=str(color1)
        self.square=float(square1)
    def display(self):
        print("Color=",self.color," Square=",self.square)

class Bedroom(Room):
    def __init__(self,color1,square1):
        self.color=float(color1)
        self.square=float(square1)
    def display(self):
        print("Color=",self.color," Square=",self.square)
    
        
