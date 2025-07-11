using System;

namespace HW4
{
    public class HW4Methods
    {
        static void Text(int integer, string text)
        {
            // Print out what the integer and string that the user entered was
            Console.WriteLine($"\nThe integer is {integer}, and the string is '{text}'.\n\n");
        }

        static string Age_Description(int age)
        {
            // Categorize the user's age, and return a description based on the category
            string conclusion = "";
            if (age >= 0 && age < 2)
            {
                conclusion = "\nYou are an infant!\n\n";
            }
            else if (age >= 2 && age < 5)
            {
                conclusion = "\nYou are a toddler!\n\n";
            }
            else if (age >= 5 && age < 13)
            {
                conclusion = "\nYou are a child!\n\n";
            }
            else if (age >= 13 && age < 20)
            {
                conclusion = "\nYou are a teenager!\n\n";
            }
            else if (age >= 20 && age < 40)
            {
                conclusion = "\nYou are an adult!\n\n";
            }
            else if (age >= 40 && age < 60)
            {
                conclusion = "\nYou are a middle-aged adult!\n\n";
            }
            else if (age >= 60)
            {
                conclusion = "\nYou are a senior adult!\n\n";
            }
            else
            {
                conclusion = "\nSorry, your age category is not known.\n\n";
            }

            return conclusion;
        }

        static void Swap(ref int a, ref int b)
        {
            // Swap the two given integers

            int temp = a;
            a = b;
            b = temp;
        }

        static int Fibonacci(int n)
        {
            // Calculate the nth number in the fibonacci sequence

            if (n <= 1)
            {
                return n;
            }

            int a = 0, b = 1, c = 0;

            for (int i = 2; i <= n; i++)
            {
                c = a + b;
                a = b;
                b = c;
            }

            return c;
        }

        static bool IsPrime(int n)
        {
            // Determine if n is prime
            if (n <= 1)
            {
                return false;
            }

            for (int i = 2; i <= Math.Sqrt(n); i++)
            {
                if (n % i == 0)
                    return false;
            }

            return true;
        }

        static void Main(string[] args)
        {
            // Void Method:
            Console.WriteLine("Void Method Demo:\n");

            // Have the user enter an integer and string
            Console.Write("Please enter an integer to be printed: ");
            int integer = int.Parse(Console.ReadLine());

            Console.Write("Please enter a string to be printed: ");
            string text = Console.ReadLine();

            // Call the method to print text containing the integer and string
            Text(integer, text);


            // Data Return:
            Console.WriteLine("Data Returning Demo:\n");

            // Have the user provide their age in years
            Console.Write("What is your age (in years)?: ");
            int age = int.Parse(Console.ReadLine());

            // Categorize their age using 'Age_Description'
            string age_desc = Age_Description(age);

            // Print out the result
            Console.WriteLine(age_desc);


            // Swap Method Demo:
            Console.WriteLine("Swap Method Demo:\n");

            // Have the user enter two integers to be swapped
            Console.Write("Enter the first integer to swap: ");
            int a = int.Parse(Console.ReadLine());

            Console.Write("Enter the second integer to swap: ");
            int b = int.Parse(Console.ReadLine());

            // Print the integers before swapping
            Console.WriteLine($"\nBefore Swap: ");
            Console.WriteLine($"First Integer, a = {a}, Second Integer, b = {b}");

            // Call the Swap method
            Swap(ref a, ref b);

            // Print the integers after swapping
            Console.WriteLine($"\nAfter Swap: ");
            Console.WriteLine($"First Integer, a = {a}, Second Integer, b = {b}\n\n");


            // Fibonacci Method Demo:
            Console.WriteLine("Fibonacci Number Method Demo:");

            // Have the user enter an integer to use for finding the nth Fibonacci number
            Console.Write("\nEnter an integer to use for finding the nth Fibonacci number: ");
            int n = int.Parse(Console.ReadLine());

            // Call the Fibonacci method
            int fib = Fibonacci(n);

            // Print the nth Fibonacci number
            Console.WriteLine($"\nThe {n}th Fibonacci number is {fib}\n\n");


            // Prime Number Demo:
            Console.WriteLine("Prime Number Demo:");


            // Have the user enter an integer to check if it is prime
            Console.Write("\nEnter an integer to check if it is prime: ");
            int p = int.Parse(Console.ReadLine());

            // Check if the given integer is prime
            bool prime = IsPrime(p);

            if (prime)
            {
                Console.WriteLine($"\n{p} is a prime number.");
            }
            else
            {
                Console.WriteLine($"\n{p} is not a prime number.");
            }
        }
    }
}
