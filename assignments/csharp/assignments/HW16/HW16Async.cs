using System;

namespace HW16
{
    public class HW16Async
    {
        static bool Prime(int num)
        {
            // Method to check if the current number is prime
            if (num <= 1)
            {
                return false;
            }
            
            for (int i = 2; i <= Math.Sqrt(num); i++)
            {
                if (num % i == 0) return false;
            }
            return true;
        }

        static Task PrimeNumbers()
        {
            // Method to identify and print all prime numbers between 2 and 26
            return Task.Run(() =>
            {
                for (int i = 2; i < 26; i++)
                {
                    if (Prime(i))
                    {
                        Console.WriteLine($"Prime Number:  {i}");
                        Task.Delay(90).Wait();
                    }
                }
            });
        }

        static Task CorrespondingLetters()
        {
            // Method to identify prime numbers between 2 and 26, and translate them into their corresponding letters
            return Task.Run(() =>
            {
                for (int i = 2; i < 26; i++)
                {
                    if (Prime(i))
                    {
                        char letter = (char)('A' + (i - 1) % 26);
                        Console.WriteLine($"Corresponding Letter:  {letter}");
                        Task.Delay(50).Wait();
                    }
                }
            });
        }

        static async Task Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Async Demo:\n");

            // Define a task variable for each of the methods
            Task Numbers = PrimeNumbers();
            Task Letters = CorrespondingLetters();

            // Execute the tasks asynchronously
            await Numbers;
            await Letters;
        }
    }
}
