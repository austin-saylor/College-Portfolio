using System;

namespace HW2
{
    public class HW2Conditionals
    {
        static string Tax(double income)
        {
            // Calculate and print tax based on the table provided in D2L
            if (income < 10000)
            {
                double tax = (income*0.05);
                return $"Tax: ${tax.ToString("0.00")}";
            }
            else if (income >= 10000 && income <= 100000)
            {
                double tax = (income*0.097);
                return $"Tax: ${tax.ToString("0.00")}";
            }
            else
            {
                double tax = (income*0.14);
                return $"Tax: ${tax.ToString("0.00")}";
            }
        }

        static void PrintShapes(int lines)
        {
            // Print Triangle
            for (int i = 0; i < lines; i++)
            {
                for (int j = 0; j < i+1; j++)
                {
                    Console.Write("*");
                }
                Console.WriteLine("\n");
            }

            Console.WriteLine("\n");

            // Print Inverted Triangle
            for (int i = (lines-1); i > -1; i--)
            {
                for (int j = 0; j < i+1; j++)
                {
                    Console.Write("*");
                }
                Console.WriteLine("\n");
            }

            Console.WriteLine("\n");

            // Print Square
            for (int i = 0; i < lines; i++)
            {
                for (int j = 0; j < lines; j++)
                {
                    Console.Write("*");
                }
                Console.WriteLine("\n");
            }
        }

        static void Main(string[] args)
        {
            // Start with the Tax Demo:
            Console.WriteLine("Tax Demo:\n");

            // Get income from user, and print it
            double income;
            Console.Write("Please enter your income: ");
            income = Single.Parse(Console.ReadLine());
            Console.WriteLine($"Income: ${income.ToString("0.00")}");

            // Get the tax amount, and print it
            string tax_str = Tax(income);
            Console.WriteLine(tax_str);

            // Transition to the Triangle Demo:
            Console.WriteLine("\nTriangle Demo:\n");

            // Get the number of lines from user
            Console.Write("Please enter the number of lines for the triangles: ");
            string lines_input = Console.ReadLine();
            int lines = int.Parse(lines_input);

            Console.WriteLine("\nHere is the output:");
            PrintShapes(lines);
        }
    }
}