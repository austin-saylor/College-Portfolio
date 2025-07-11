using System;

namespace HW15
{
    public class Car
    {
        // Class (object) defining a car object
        public string color
        {
            // Getter/Setter method for 'color'
            get;
            set;
        }
    }

    public class Lambda
    {
        public void NegativeNumbers(List<int> nums)
        {
            // Method to filter a list of numbers and find the negatives
            var negativeNumbers = nums.FindAll(n => n < 0);
            Console.WriteLine("\nNegative Numbers: " + string.Join(", ", negativeNumbers));
        }

        public void NumberSquares(List<int> nums)
        {
            // Method to find the squares of the numbers in the given list
            var squares = nums.Select(n => n * n).ToList();
            Console.WriteLine("\nSquares: " + string.Join(", ", squares));
        }

        public void StringLength(List<string> strs)
        {
            // Method to list the strings in the given list in order based on their length
            var orderedWords = strs.OrderBy(w => w.Length).ToList();
            Console.WriteLine("\nWords Ordered by Length: " + string.Join(", ", orderedWords) + "\n");
        }
    }

    public class Linq
    {
        public static void ColorSortCars(List<Car> cars)
        {
            // Method to sort the cars in the given list by their color
            var sortedCars = from car in cars
                             orderby car.color
                             select car;
            Console.WriteLine("\nCars Sorted by Color: " + string.Join(", ", sortedCars.Select(car => car.color)));
        }

        public static void SortAscending(List<int> nums)
        {
            // Method to sort the numbers in the given list in ascending order
            var sortedNumbers = from num in nums
                                orderby num
                                select num;
            Console.WriteLine("\nNumbers Sorted in Ascending Order: " + string.Join(", ", sortedNumbers));
        }

        public static void Alphabetize(List<string> strs)
        {
            // Method to sort the strings in the given list alphabetically
            var sortedStrings = from str in strs
                                orderby str
                                select str;
            Console.WriteLine("\nStrings Sorted Alphabetically: " + string.Join(", ", sortedStrings));
        }
    }

    public class HW15Linq
    {
        public static void Main()
        {
            // Start the program
            Console.WriteLine("Lambda and LINQ Demo:\n");

            // Define the lists to be used throughout the examples
            List<int> nums = new List<int> { -100, 72, 85, -84, 97, -40, 18, -12, 32, -2 };
            List<string> strs = new List<string> { "Wallet", "Ball", "Key", "Apple", "Car", "Plane", "Fish", "Tank", "Pool" };
            List<Car> cars = new List<Car>
            {
                new Car {color = "Red"},
                new Car {color = "White"},
                new Car {color = "Black"},
                new Car {color = "Blue"},
                new Car {color = "Yellow"},
                new Car {color = "Red"},
                new Car {color = "Orange"},
                new Car {color = "Yellow"},
                new Car {color = "Red"},
                new Car {color = "White"},
                new Car {color = "Black"}
            };

            // Define an instance of the lambda class
            Lambda lambda_demo = new Lambda();

            // Print the lists being used for the user's viewing:
            Console.WriteLine("\nLists Being Used:");
            Console.WriteLine("\n'nums': " + string.Join(", ", nums));
            Console.WriteLine("'strs': " + string.Join(", ", strs));
            Console.WriteLine("'cars' (listing the color property of each): " + string.Join(", ", cars.Select(car => car.color)));

            // Transitition to the Lambda demos
            Console.WriteLine("\n\nLambda Demo:");

            // Demonstrate the Lambda methods
            lambda_demo.NegativeNumbers(nums);
            lambda_demo.NumberSquares(nums);
            lambda_demo.StringLength(strs);

            // Transition to the LINQ demos
            Console.WriteLine("\nLINQ Demo:");

            // Demonstrate the LINQ methods
            Linq.ColorSortCars(cars);
            Linq.SortAscending(nums);
            Linq.Alphabetize(strs);
        }
    }
}
