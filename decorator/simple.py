def simple_decorator(f):
    def wrapper():
        print("Entering Function")
        f()
        print("Exited Function")
    return wrapper


# @simple_decorator
def hello():
    print("Hello World")


x = simple_decorator(hello)
x()