class Operation:
    def __init__(self, number1,number2):
        self.number1=number1
        self.number2=number2

    def add(self,number1,number2):
        return self.number1+self.number2

instance = Operation(25,56)
print(instance.number1)
print(instance.number2)

print(instance.add(25,56))