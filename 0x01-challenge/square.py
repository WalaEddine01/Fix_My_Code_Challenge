#!/usr/bin/python3
"""
Module contains a square class
"""


class Square:
    """
    square class
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        creating an obj
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """
        Permiter Of Square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        printing the infos of a square
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """
    creating square
    """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
