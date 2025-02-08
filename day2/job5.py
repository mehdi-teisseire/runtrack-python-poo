class Car:
    def __init__(self,brand,model,year,kilometers):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kilometers = kilometers
        self.status = False
        self.__reserve = 50
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_kilometers(self):
        return self.__kilometers
    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self,model):
        self.__model = model
    def set_years(self,year):
        self.__year = year  
    def set_kilometers(self,kilometers):
        self.__kilometers = kilometers
   
    def stop(self):
        self.status = False
    def get_reserve(self):
        return self.__reserve
    def start(self,reserve):
        if reserve > 5:
            self.status = True
            return 'Car is running'
        else:
            return 'Not enough fuel'
    def __str__(self):
        return 'The car is a ' + self.__brand + ' ' + self.__model + ' from ' + str(self.__year) + ' with ' + str(self.__kilometers) + ' kilometers'

car = Car('Toyota','Corolla',2015,100000)
print(str(car))
print(car.get_reserve())
print(car.start(20))
print(car.start(0))