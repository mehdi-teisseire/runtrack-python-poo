class City:
    def __init__(self, name, population):
        self.__name = name
        self.__population = population
    
    def get_city(self):
        return self.__name
    
    def get_population(self):
        return self.__population

class Person:
    def __init__(self, name, age, population):
        self.__name = name
        self.__age = age
        self.__population = population
    
    def get_person(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def add_people(self):
        return self.__population.get_population() + 1

paris = City("Paris", 1000000)
print(paris.add_people()) 

marseille = City("Marseille", 861635)
print(marseille.get_population())