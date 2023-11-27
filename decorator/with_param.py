def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return round(func(a, b), 0)

    return inner

@smart_div
def div(a, b):
    return a / b

result = div(30, 40)
print(result)
