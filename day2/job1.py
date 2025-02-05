class Rectangle:
    def __init__(self,width, height):
        self.width__ = width
        self.height__ = height
    
    def set_rectangle(self, width, height):
        self.width__ = width
        self.height__ = height
    
    def get_rectangle(self):
        return self.width__ , self.height__
    

    
r = Rectangle(23,21)
print(r.get_rectangle())
r.set_rectangle(12,10)
print(r.get_rectangle())