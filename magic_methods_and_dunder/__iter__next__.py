class CountingNumbers:
    def __init__(self, limit):
        """
        Initializes an instance of the class.

        Args:
            limit (int): The maximum value that the 'current' attribute can have.

        Returns:
            None
        """
        self.limit = limit
        self.current = 0

    def __iter__(self):
        """
        Returns an iterator object of the class.

        Parameters:
            None

        Returns:
            Iterator: The iterator object of the class.
        """
        return self

    def __next__(self):
        """
        Return the next element in the iterator.

        Returns:
            int: The next element in the iterator.

        Raises:
            StopIteration: If the limit has been reached and there are no more elements to return.
        """
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
