import unittest
from point import Point
from polygon import Polygon

polygon = Polygon()


class Test(unittest.TestCase):
    def test_rectangle(test) -> None:
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(0, 1))
        polygon.add_point(Point(2, 1))
        polygon.add_point(Point(2, 0))

        test.assertEqual(polygon.calculate_area(), 3.5)

    def test_dodecagon(test) -> None:
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(-1, 1))
        polygon.add_point(Point(-1.5, 2))
        polygon.add_point(Point(-1.5, 4))
        polygon.add_point(Point(-1, 5))
        polygon.add_point(Point(0, 6))
        polygon.add_point(Point(2, 6))
        polygon.add_point(Point(3, 5))
        polygon.add_point(Point(3.5, 4))
        polygon.add_point(Point(3.5, 2))
        polygon.add_point(Point(3, 1))
        polygon.add_point(Point(2, 0))

        test.assertEqual(polygon.calculate_area(), 25.0)

    def test_star(test) -> None:
        polygon.add_point(Point(0, 50))
        polygon.add_point(Point(10, 25))
        polygon.add_point(Point(35, 25))
        polygon.add_point(Point(15, 10))
        polygon.add_point(Point(25, -10))
        polygon.add_point(Point(0, 0))
        polygon.add_point(Point(-25, -10))
        polygon.add_point(Point(-15, 10))
        polygon.add_point(Point(-35, 25))
        polygon.add_point(Point(-10, 25))

        test.assertEqual(polygon.calculate_area(), 4487.5)


if __name__ == '__main__':
    unittest.main()
