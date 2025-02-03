import math

class Cercle:
    def __init__(self, radius):
        self.radius = radius
    
    def changeRadius(self, new_radius):
        self.radius = new_radius
    
    def display(self):
        print(f"Rayon : {self.radius}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aera()}")
    
    def circonference(self):
        return 2 * math.pi * self.radius
    
    def aera(self):
        return math.pi * (self.radius ** 2)
    
    def diametre(self):
        return 2 * self.radius


cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Informations du cercle 1 :")
cercle1.display()

print("\nInformations du cercle 2 :")
cercle2.display()
