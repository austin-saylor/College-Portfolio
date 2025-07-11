"""
The main module. This module contains the 'Results' class,
and the code that calls the rest of the program.
"""

from point import Point
from polygon import Polygon


class Results:
    """
    Results class to organize and print the results.
    """
    def __init__(self, n: int) -> None:
        """
        Initialize an instance of the 'Results' class
        """
        self.__n = n

    @property
    def n(self) -> int:
        """
        Getter method for the 'n' variable
        """
        return self.__n

    def generate(self) -> list[float]:
        """ Generate a list of areas for each polygon. """
        # A list to store the areas of each polygon
        area_list: list[float] = []

        for m in range(self.n):
            # User inputs the number of points, and the coordinates of each one
            line = input().split()[1:]

            # A list to store the x coordinates
            x_coords = [float(x) for x in line[::2]]

            # A list to store the y coordinates
            y_coords = [float(x) for x in line[1::2]]

            area = float(0)  # A variable to store the area of the polygon
            polygon = Polygon()
            for p in range(len(x_coords)):
                polygon.add_point(Point(x_coords[p], y_coords[p]))

            # After all data on the polygon is collected, calculate the area
            area = polygon.calculate_area()
            area_list.append(area)  # Add the area to 'area_list'

        return area_list


if __name__ == "__main__":
    """
    Define the number of polygons,
    generate a list of their areas, and print them.
    """
    n = int(input())  # User defines the number of polygons

    results = Results(n)

    # Generate a list of areas for each polygon
    polygon_areas = results.generate()

    # Print out the areas of each polygon:
    for a in range(len(polygon_areas)):
        print(polygon_areas[a])
