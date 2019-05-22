class Shape:
    area = 0
    def Area(self):
        print(self.area)
    
class Square(Shape):
    def __init__(self,l):
        self.l = l

    def Area(self):
        print(self.l*self.l)

x = Shape()
x.Area()
x = Square(5)
x.Area()
