using System;

namespace HW3
{
    public class HW3Arrays
    {
        static int[] Generate_Array()
        {
            // Define the array
            int[] randomValues = new int[10];
            
            // Initialize the random class
            Random rand = new Random();
            
            // Assign random values to the array indices
            for (int i = 0; i < randomValues.Length; i++)
            {
                randomValues[i] = rand.Next(0, 101); // Random number between 0 and 100
            }

            return randomValues;
        }

        static void Print_Array(int[] randomValues)
        {
            Console.WriteLine("Random values:");
            foreach (int value in randomValues)
            {
                Console.WriteLine(value);
            }
            Console.WriteLine("\n");
        }

        static void Print_Sorted_Arrays(int[] randomValues)
        {
            // Sort the array in ascending order
            Array.Sort(randomValues);

            // Print the array sorted in ascending order
            Console.WriteLine("Random values (Ascending Order):");
            foreach (int value in randomValues)
            {
                Console.WriteLine(value);
            }
            Console.WriteLine("\n");

            // Reverse the array
            Array.Reverse(randomValues);

            // Print the array sorted in descending order
            Console.WriteLine("Random values (Descending Order):");
            foreach (int value in randomValues)
            {
                Console.WriteLine(value);
            }
            Console.WriteLine("\n");
        }

        static int[,] Generate_Matrix()
        {
            // Define a 2-D array with 3 rows, 3 cols
            int[,] matrix = new int[3, 3];

            // Assign values to the indices of the matrix
            int index = 0;
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    index += 1;
                    matrix[i, j] = index;
                }
            }

            return matrix;
        }

        static void Print_Matrix(int[,] matrix)
        {
            Console.WriteLine("3x3 Array:");
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    Console.Write(matrix[i, j] + " ");
                }
                Console.WriteLine();
            }
            Console.WriteLine("\n");
        }

        static int[][] Generate_Jagged_Array()
        {
            // Define the jagged array with 5 rows
            int[][] jagged_array = new int[5][];
            
            // Initialize an instance of the random class
            Random rand = new Random();
            
            // Generate the jagged array
            for (int i = 0; i < jagged_array.Length; i++)
            {
                int columns = rand.Next(1, 6); // Random number between 1 and 5
                jagged_array[i] = new int[columns]; // Define the sub array with the given number of columns
                int index = 0;
                
                // Assign values to each index of the current sub array
                for (int j = 0; j < columns; j++)
                {
                    index += 1;
                    jagged_array[i][j] = index;
                }
            }

            return jagged_array;
        }

        static void Print_Jagged_Array(int[][] jagged_array)
        {
            Console.WriteLine("Jagged Array:");
            for (int i = 0; i < jagged_array.Length; i++)
            {
                for (int j = 0; j < jagged_array[i].Length; j++)
                {
                    Console.Write(jagged_array[i][j] + " ");
                }
                Console.WriteLine();
            }
        }

        static void Main(string[] args)
        {
            // Generate the Single-Dimensional Array
            int[] randomValues = Generate_Array();

            // Start with the Single-Dimensional Array Demo:
            Console.WriteLine("BASIC ARRAY DEMO: \n");
            
            // Print the array
            Print_Array(randomValues);

            // Print the sorted versions of the array
            Print_Sorted_Arrays(randomValues);

            // Transition to Multi-Dimensional Array Demo:
            Console.WriteLine("\nMULTI-DIMENSIONAL ARRAY DEMO: \n");

            // Generate a 3x3 rectangular array (matrix)
            int[,] matrix = Generate_Matrix();

            // Print the matrix
            Print_Matrix(matrix);

            // Generate a Jagged Array, with 5 rows and a random number of columns
            int[][] jagged_array = Generate_Jagged_Array();

            // Print the jagged array
            Print_Jagged_Array(jagged_array);
        }
    }
}
