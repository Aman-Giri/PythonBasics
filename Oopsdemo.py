# Classes are the User defined prototype/BluePrint
# Self Keyword is mandatory for calling variables names into method
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# new keyword is not required when you create any Object in python
class Calculator:
    num = 100 # Class Variable
    #default Constructor

    def __init__(self,a,b):
        self.firstNumber = a # instance Variable
        self.secondNumber = b # instance Variable
        print("I am called automatically when the Object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def summation(self):
        return self.firstNumber+self.secondNumber + Calculator.num # we can use self also for calling the class variable


obj = Calculator(2, 3)  # Syntax to create the Object in Python
obj.getData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.summation())

