using System;

namespace HW14
{
    // CircleCalc class to calculate area and circumference of a circle
    public class CircleCalc
    {
        public void CircleArea(double radius)
        {
            // Method to calculate the area of the circle
            double area = Math.PI * radius * radius;
            area = Math.Round(area, 2);
            Console.WriteLine($"\nArea = {area}");
        }

        public void Circumference(double radius)
        {
            // Method to calculate the circumference of the circle
            double circumference = 2 * Math.PI * radius;
            circumference = Math.Round(circumference, 2);
            Console.WriteLine($"Circumference = {circumference}");
        }
    }

    // Delegate to handle circle calculations
    public delegate void CircleDelegate(double radius);

    public class DelegateTypes
    {
        public static string FuncDemo(string line)
        {
            if (string.IsNullOrEmpty(line))
                return line;

            string result = line.ToUpper();
            return $"Func Result: {result}";
        }

        public static void ActionDemo(string line)
        {
            // Method to demonstrate the 'Action' delegate type
            Console.WriteLine($"Action Result: {line}");
        }

        public static bool PredicateDemo(int num)
        {
            // Method to demonstrate the 'Predicate' delegate type
            bool result = (num % 10 == 0);
            Console.WriteLine($"\nPredicate Result: {result}");
            if (result == false)
            {
                Console.WriteLine($"The given number is not divisible by 10.");
            }
            else
            {
                Console.WriteLine($"The given number is divisible by 10.");
            }
            return result;
        }
    }

    public class HW14Delegates
    {
        public static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Delegates Demo:\n");
            Console.WriteLine("Circle Calculations:\n");

            // Define the multi-cast delegate
            CircleCalc calculate = new CircleCalc();
            CircleDelegate circleDelegate = calculate.CircleArea;
            circleDelegate += calculate.Circumference;

            // Ask the user for a radius
            double radius = 0;
            bool isValidDouble = false;

            while (!isValidDouble)
            {
                Console.Write("Please enter a radius: ");
                string userInput = Console.ReadLine();

                if (double.TryParse(userInput, out radius))
                {
                    isValidDouble = true;
                }
                else
                {
                    Console.WriteLine("The input is not a valid double. Please try again.");
                }
            }

            // Use the delegate to call the calculation methods using the given radius
            circleDelegate(radius);

            // Transition to demonstrating built-in Delegate Types:
            Console.WriteLine("\n\nBuilt-In Types Demo:");

            // Func Example
            Func<string, string> Cap = DelegateTypes.FuncDemo;
            Console.Write("\nPlease enter a string to be used in the Func Demo: ");
            string func_line = Console.ReadLine();
            Console.WriteLine(Cap(func_line));

            // Action Example
            Action<string> PrintMessage = DelegateTypes.ActionDemo;
            Console.Write("\nPlease enter a string to be used in the Action Demo: ");
            string action_line = Console.ReadLine();
            PrintMessage(action_line);

            // Predicate Example
            Predicate<int> DivisibleByTen = DelegateTypes.PredicateDemo;
            int num = 0;
            bool isValidInt = false;

            while (!isValidInt)
            {
                Console.Write("\nPlease enter a number to be used for the Predicate Demo: ");
                string userInput = Console.ReadLine();

                if (int.TryParse(userInput, out num))
                {
                    isValidInt = true;
                }
                else
                {
                    Console.WriteLine("The input is not a valid integer. Please try again.");
                }
            }
            DivisibleByTen(num);
        }
    }
}