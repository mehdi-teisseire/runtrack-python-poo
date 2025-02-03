class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name)
    def older(self):
        self.age += 1
        return self.age

dog1 = Animal("Rex", 0)
print(dog1.older())
print(dog1.older())
dog1.display()