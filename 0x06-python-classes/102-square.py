#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size: length of the side of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square.

        Raises:
            TypeError: size is not an integer
            ValueError: size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Defines the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison to a Square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Defines the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison to a Square."""
        return self.area() <= other.area()
