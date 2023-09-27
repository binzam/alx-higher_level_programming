#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size: length of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the size of the square.

        Raises:
            TypeError: size is not an integer
            ValueError: size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
            size squared
        """
        return self.__size ** 2

    def my_print(self):
        """Print this square with the # character."""
        for i in range(0, self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
            print()
