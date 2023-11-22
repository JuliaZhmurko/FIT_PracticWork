class Room:
    name = ''
    color = ''
    length = 0.0
    breadth = 0.0

    def CreateRoom(self,name,color,length,breadth):
        self.name=str(name)
        self.color=str(color)
        self.length=float(length)
        self.breadth=float(breadth)

    def calculate_area(self):
        print("Площа кімнати : ",self.length * self.breadth)
        
    def display(self):
        print("Відображення назви та кольору name = ",self.name,"; color = ", self.color)

class Bedroom(Room):
    def bedroom__method(self):
        print("Цей метод з дочірнього класу")
        
    def display(self):
        print("name = ",self.name,"; color = ", self.color)