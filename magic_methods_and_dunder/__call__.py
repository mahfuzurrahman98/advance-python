class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        # Define the behavior when an instance is called
        return x * self.factor


# Create an instance of Multiplier
double = Multiplier(2)

# Use the instance as if it were a function
result = double(5)
print(result)  # Output: 10
