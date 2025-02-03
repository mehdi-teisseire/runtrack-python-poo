class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def display(self):
        print("Name:", self.name)
        print("Surname:", self.surname)

p1 = person("John", "Doe")
p2 = person("Jane", "Doe")

person.display(p1)
person.display(p2)