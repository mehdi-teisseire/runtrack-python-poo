class Coordonate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def both(self):
        print("x:", self.x)
        print("y:", self.y)
    
    def display(self):
        print("x:", self.x)
    
    def change(self, x, y):
        self.x = x
        self.y = y
        print("x:", self.x)
        print("y:", self.y)


c1 = Coordonate(5, 6)

c1.both()
c1.display()
c1.change(7, 8)

