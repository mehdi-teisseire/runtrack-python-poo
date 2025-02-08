class Part :
    def __init__(self,name,material):
        self.name = name
        self.material = material

    def change_material(self):
        self.material = "plastic"
        return self.material

boat = Part("boat","wood")
print(boat.material)
print(boat.name)
print(boat.change_material())