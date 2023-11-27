# square = lambda x: x**2

def function_builder(n):
    return lambda x: x**n

# make a function that takes a function and a number
def inc_by_two(func, num):
    return func(num) + 2

square = function_builder(2)
cube = function_builder(3)

# print(square(2))
# print(cube(2))

print(inc_by_two(square, 3))