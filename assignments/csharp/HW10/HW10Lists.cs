using System;
using System.Collections.Generic;

namespace HW10
{
    public class HW10Lists
    {
        // Initialize the lists
        static List<int> IntList = new List<int>();
        static List<string> StrList = new List<string>();

        static void Insert<T>(List<T> list, T value)
        {
            // Insert the given item into the given list using BinarySearch
            int index = list.BinarySearch(value);
            if (index < 0) index = ~index;
            list.Insert(index, value);
        }

        static void PrintList<T>(List<T> list)
        {
            // Print the given list

            Console.Write("[");

            foreach (T item in list)
            {
                Console.Write($"{item}  ");
            }

            Console.Write("]\n");
        }
        
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("List Demo:\n");

            // Print out the lists in their original form
            Console.Write("Original int list: ");
            PrintList(IntList);

            Console.Write("Original string list: ");
            PrintList(StrList);

            // Populate the integer list
            Insert(IntList, 10);
            Insert(IntList, 640);
            Insert(IntList, 40);
            Insert(IntList, 5120);
            Insert(IntList, 320);
            Insert(IntList, 160);
            Insert(IntList, 1280);
            Insert(IntList, 80);
            Insert(IntList, 2560);
            Insert(IntList, 20);

            // Populate the string list
            Insert(StrList, "Strawberry");
            Insert(StrList, "Beautiful");
            Insert(StrList, "Red");
            Insert(StrList, "Blue");
            Insert(StrList, "Dog");
            Insert(StrList, "Cat");
            Insert(StrList, "Day");
            Insert(StrList, "Mountain");
            Insert(StrList, "Fire");
            Insert(StrList, "Ice");

            // Print the lists as they are after being populated
            Console.Write("\nInt list after insertion: ");
            PrintList(IntList);

            Console.Write("String list after insertion: ");
            PrintList(StrList);
        }
    }
}
