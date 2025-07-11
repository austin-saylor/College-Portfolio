using System;

namespace HW1
{
    public class HW1Types
    {
        static void Main(string[] args)
        {
            // Introduce the problem
            string problem_desc = "This program demonstrates typing in C#, and uses Heron's Formula to calculate the area of a triangle.\n";
            Console.WriteLine(problem_desc);
            Console.WriteLine("Typing Demo:\n");

            // Define type variables:
            int int_var = 10;
            char char_var = 'A';
            string str_var = "Circle";
            double double_var = 1000000.8906;

            // Define and print description strings:
            string int_desc = $"Integer-type variable: int_var = {int_var}";
            string char_desc = $"Character-type variable: char_var = {char_var}";
            string str_desc = $"String-type variable: str_var = {str_var}";
            string double_desc = $"Double-type variable: double_var = {double_var}";

            Console.WriteLine("Original Values:");
            Console.WriteLine(int_desc);
            Console.WriteLine(char_desc);
            Console.WriteLine(str_desc);
            Console.WriteLine(double_desc);

            // Change the values type variables:
            int_var = 20;
            char_var = 'Z';
            str_var = "Triangle";
            double_var = 500000000000.6265;

            // Define and print new description strings:
            int_desc = $"Integer-type variable: int_var = {int_var}";
            char_desc = $"Character-type variable: char_var = {char_var}";
            str_desc = $"String-type variable: str_var = {str_var}";
            double_desc = $"Double-type variable: double_var = {double_var}";

            Console.WriteLine("\nNew Values:");
            Console.WriteLine(int_desc);
            Console.WriteLine(char_desc);
            Console.WriteLine(str_desc);
            Console.WriteLine(double_desc);

            // Transition to the Heron's Formula demo:
            Console.WriteLine("\nHeron's Formula Demo:\n");

            // Define side lengths:
            double a = 4;
            double b = 5;
            double c = 6;

            // Define semi-perimeter:
            double S = (a + b + c) / 2;

            // Define area using Heron's formula:
            double area = Math.Abs(Math.Sqrt(S * (S - a) * (S - b) * (S - c)));

            // Define a rounded version of the area using int:
            int rounded_area = (int)Math.Round(area);

            // Print the answer:
            string sides = $"The values of the sides are: a = {a}, b = {b}, c = {c}";
            string semi_perim = $"The semi-perimeter, S, is equal to {S}";
            string answer = $"\nThe area of the triangle is {area} cm². When rounded to the nearest whole number, it is equal to {rounded_area}.";
            
            Console.WriteLine(sides);
            Console.WriteLine(semi_perim);
            Console.WriteLine(answer);
        }
    }
}
