class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'
    
    def __del__(self):
        print(f'{self.name} is being deleted')

p = Person('John', 78)
print(p)


