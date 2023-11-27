def my_generator(size):
    for i in range(1, size + 1):
        yield i

# Creating a generator with a size of 5
gen = my_generator(3)

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("Generator is exhausted")