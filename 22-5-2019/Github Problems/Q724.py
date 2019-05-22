class Rectangle(object):
    def __init__(self,l,w):
        self.l=l
        self.w=w
        self.area()

    def area(self):
        print("The area is:")
        print(self.l*self.w)

r = Rectangle(5,5)