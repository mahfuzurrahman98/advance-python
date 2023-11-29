# make a class with one public attribute and one protected attribute

class MyClass:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}'

mc = MyClass('x-data', 'y-data')
print(mc)
mc.z = 'z-data'
print(mc.z)