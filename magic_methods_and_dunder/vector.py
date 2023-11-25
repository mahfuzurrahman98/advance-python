class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


v1 = Vector(10, 20)
v2 = Vector(30, 40)
v3 = v1 + v2

print("v3:")
print(v3)

# eval the repr and make a new object
v4 = eval(repr(v3))

print("v4:")
print(v4)
