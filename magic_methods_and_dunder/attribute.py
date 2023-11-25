class DynamicAttributes:
    def __init__(self):
        # Initialize attributes directly to avoid calling __setattr__
        object.__setattr__(self, 'attributes', {})

    def __getattribute__(self, name):
        # Bypass the custom __getattribute__ for 'attributes'
        if name == 'attributes':
            return object.__getattribute__(self, 'attributes')

        try:
            return object.__getattribute__(self, 'attributes')[name]
        except KeyError:
            raise AttributeError(f"'DynamicAttributes' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        # Bypass the custom __setattr__ for 'attributes'
        if name == 'attributes':
            object.__setattr__(self, 'attributes', value)
        else:
            object.__getattribute__(self, 'attributes')[name] = value

# Create an instance of DynamicAttributes
obj = DynamicAttributes()

# Assign attributes dynamically
obj.color = "red"
obj.size = 10

# Access attributes dynamically
print(obj.color)  # Output: red
print(obj.size)   # Output: 10
print(obj.weight)  # Raises AttributeError: 'DynamicAttributes' object has no attribute 'weight'
