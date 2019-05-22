class test:

    def __init__(self):
        self.inp=""
        self.getString()
        self.printString()
    def getString(self):
        self.inp = input("Enter a string:\n")
    
    def printString(self):
        print(self.inp.upper())

x = test()
