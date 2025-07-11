"""
The point module. This module defines all of the
polygon points.
"""


class Point:
    """
    Create a new point for the polygon.

    Various elements of code in this class were sourced from the
    "WhenToUseOOP" Jupyter Notebook, and ChatGPT 4, with the following prompt:

    "Using python 3, can you solve the kattis problem-
    convex polygon area, using object-oriented design? Please use getter
    and setter methods for each attribute where appropriate."
    """
    def __init__(self, x: float, y: float) -> None:
        """ Initialize an instance of the 'Point' class."""
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        """ Get the state of the x-coordinate property. """
        return self.__x

    @x.setter
    def x(self, value: float) -> None:
        """ Set the value of the x-coordinate. """
        if not isinstance(value, float):
            raise ValueError("x must be a float")
        self.__x = value

    @property
    def y(self) -> float:
        """ Get the state of the y-coordinate property. """
        return self.__y

    @y.setter
    def y(self, value: float) -> None:
        """ Set the value of the y-coordinate """
        if not isinstance(value, float):
            raise ValueError("y must be a float")
        self.__y = value
