class SquareSeries:
    def __init__(self, length):
        self.length = length

    def __getitem__(self, index):
        if 0 <= index < self.length:
            return index ** 2
        else:
            raise IndexError("Index out of range")

# Create an instance of SquareSeries
squares = SquareSeries(5)

# Access elements using indexing
print(squares[0])  # Output: 0
print(squares[1])  # Output: 1
print(squares[2])  # Output: 4
print(squares[3])  # Output: 9
print(squares[4])  # Output: 16
print(squares[5])  # IndexError: Index out of range