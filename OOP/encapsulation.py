# make a perfact example of encapsulation
# encapsulation is a process of binding data and function together
# it is also called data hiding
# it is used to restrict access to methods and variables
# this prevent data from direct modification which is called encapsulation

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.__age = 20

    def display(self):
        print(self.name)
        print(self.roll)
        print(self.__age)

    def setAge(self, age):
        self.__age = age

s = Student('John', 2)
s.name = 'John Doe'
# s.__age = 30
s.setAge(30)
s.display()