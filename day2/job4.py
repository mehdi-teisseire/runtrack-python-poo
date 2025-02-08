class Student:
    def __init__(self,name,firstname,student_id,credit):
        self.__name = name
        self.__firstname = firstname
        self.__student_id = student_id
        self.__credit = credit
        
    def add_credit(self,credit):
        if credit < 0:
            print ('Credit must be positive')
        else:
            self.__credit += credit
    
    def get_credit(self):
        return self.__credit
    def get_student_id(self):
        return self.__student_id
    def get_name(self):
        return self.__name
    def get_firstname(self):
        return self.__firstname
    
    def student_eval(self):
        if self.__credit < 30:
            return 'Student is failing'
        elif self.__credit < 60:
            return 'Student is passing'
        else:
            return 'Student is passing with distinction'
    
    def __str__(self):
        return self.__name + ' ' + self.__firstname + ' ' +str(self.__student_id) +' id' + ' has ' + str(self.__credit) + ' credits'

student = Student('john','doe',135,0)
print(student.student_eval())
student.add_credit(100)
print(student.__str__())
print(student.student_eval())