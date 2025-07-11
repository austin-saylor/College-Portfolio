using System;

namespace HW12
{
    public class CustomException : Exception
    {
        // Class to define the custom exception
        public CustomException(string msg) : base(msg) 
        { 

        }
    }

    public class HW12Exceptions
    {
        static void ThrowCustomException(string msg)
        {
            // Throw the custom exception using a given message
            throw new CustomException(msg);
        }

        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Exceptions Demo: \n");

            try
            {
                // Throw the custom exception
                string msg = "This is a custom exception.";
                ThrowCustomException(msg);
            }
            catch (CustomException ex)
            {
                // Catch and handle the custom exception
                Console.WriteLine($"Caught a custom exception: {ex.Message}");
                Console.WriteLine("Given that this exception has occurred, you should look for errors in your program.");
            }
        }
    }
}
