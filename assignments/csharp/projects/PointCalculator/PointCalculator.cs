using System;

namespace PointCalc
{

    public class Point
    {
        // Private variables for 'Point'
        private int x;
        private int y;

        public Point(int x, int y)
        {
            // Constructor
            this.X = x;
            this.Y = y;
        }

        private int X
        {
            // Getter/Setter method for X
            get { return this.x; }
            set { this.x = value; }
        }
        
        private int Y
        {
            // Getter/Setter method for Y
            get { return this.y; }
            set { this.y = value; }
        }

        public void PrintPoint()
        {
            Console.WriteLine($"({this.X}, {this.Y})");
        }

        public override string ToString()
        {
            return $"({this.X}, {this.Y})";
        }

        public static Point operator +(Point A, Point B)
        {
            // '+' Operator Overload - Adds two points together
            int newX, newY;

            Point newPoint = new Point(0, 0);

            newX = A.X + B.X;
            newY = A.Y + B.Y;

            newPoint.X = newX;
            newPoint.Y = newY;

            return newPoint;
        }

        public static Point operator *(Point A, Point B)
        {
            // '*' Operator Overload (Multiplies two points together)
            int newX, newY;

            Point newPoint = new Point(0, 0);

            // (A, B) * (C, D) = ((A*C-B*D), (A*C+B*D))
            newX = ((A.X * B.X) - (A.Y * B.Y));
            newY = ((A.X * B.X) + (A.Y * B.Y));

            newPoint.X = newX;
            newPoint.Y = newY;

            return newPoint;
        }

        public static Point operator *(Point A, int factor)
        {
            // '*' Operator Overload (Multiplies a given point by a given factor)
            int newX, newY;

            Point newPoint = new Point(0, 0);

            newX = A.X * factor;
            newY = A.Y * factor;

            newPoint.X = newX;
            newPoint.Y = newY;

            return newPoint;
        }

        public static bool operator ==(Point A, Point B)
        {
            // '==' Operator Overload - checks if two given points are equal
            if (A.X == B.X && A.Y == B.Y)
            {
                return true;
            }

            return false;
        }
        
        public static bool operator !=(Point A, Point B)
        {
            // '!=' Operator Overload - checks if two given points are different
            return !(A == B);
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Project 2 - Cartesian Point Calculator:\n\n");

            // Define two points
            Point point1 = new Point(1, 2);
            Point point2 = new Point(5, 6);

            // Define comparisons using overloaded operators
            Point sum = point1 + point2;
            Point mult_factor = point1 * 5;
            Point mult_points = point1 * point2;
            bool equality = (point1 == point2);
            bool inequality = (point1 != point2);

            // Print the result of the comparisons
            Console.WriteLine($"{point1} + {point2}:");
            sum.PrintPoint(); // Output = (6, 8)

            Console.WriteLine($"\n{point1} * 5:");
            mult_factor.PrintPoint(); // Output = (5, 10)

            Console.WriteLine($"\n{point1} * {point2}:");
            mult_points.PrintPoint(); // Output = (-7, 17)

            Console.WriteLine($"\n{point1} == {point2}:");
            Console.WriteLine(equality.ToString()); // False

            Console.WriteLine($"\n{point1} != {point2}:");
            Console.WriteLine(inequality.ToString()); // True
        }
    }
}