#!/usr/bin/python3
"""
This module defines a Square class that represents a square shape.
"""


class Square():
    """
    Represents a square shape with attributes for width, height, and methods
    to calculate the area and perimeter.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a Square object with optional width and height parameters.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculates and returns the area of the square.
        Formula: width * height
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates and returns the perimeter of the square.
        Formula: (width * 2) + (height * 2)
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square's dimensions.
        Example: "12/9" for a square with width 12 and height 9.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    # Example usage
    s = Square(width=12, height=9)
    print(s)  # Output: 12/9
    print(s.area_of_my_square())  # Output: 108
    print(s.perimeter_of_my_square())  # Output: 42
