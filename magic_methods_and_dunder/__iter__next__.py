class CountingNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration  # Stop iteration when limit is reached


# Create an instance of CountingNumbers
counting_numbers = CountingNumbers(5)

# Iterate over the counting numbers
for number in counting_numbers:
    print(number)
