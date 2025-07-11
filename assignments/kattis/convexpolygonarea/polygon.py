"""
The polygon module. This module defines all
of the polygons.
"""

from point import Point


class Polygon:
    def __init__(self) -> None:
        """
        Initialize a list to store the coordinate points of the polygon.
        """
        self.__points: list[Point] = []

    @property
    def points(self) -> list[Point]:
        """
        Getter method for the 'points' attribute.
        """
        return self.__points

    def add_point(self, point: Point) -> None:
        """ Add a new point to the point list. """
        if isinstance(point, Point):
            self.points.append(point)

    def calculate_area(self) -> float:
        """ Calculate the polygon area using the Shoelace Formula. """
        shoelace = float(0)
        for s in range(len(self.points)):
            i = (s + 1) % (len(self.points))
            shoelace += (self.points[s].x * self.points[i].y)
            shoelace -= (self.points[s].y * self.points[i].x)

        area = (1/2)*(abs(shoelace))
        return area
