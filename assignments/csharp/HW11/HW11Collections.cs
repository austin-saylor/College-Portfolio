using System;
using System.Collections.Generic;

namespace HW11
{
    public class HW11Collections
    {
        // Initialize the the collections
        static Dictionary<string, string> dict = new Dictionary<string, string>();
        static Queue<string> queue = new Queue<string>();
        static Stack<string> stack = new Stack<string>();

        static void Dequeue()
        {
            // Method to dequeue items, taking into account empty queues
            if (queue.Count > 0)
            {
                string removedItem = queue.Dequeue();
            }
            else
            {
                Console.WriteLine("Queue is empty.");
            }
        }

        static void PrintDictionary()
        {
            // Method to print the dictionary collection
            foreach (var pair in dict)
            {
                Console.WriteLine($"Item: {pair.Key},  Category: {pair.Value}");
            }
        }

        static void PrintQueue()
        {
            // Method to print the queue collection
            foreach (var item in queue)
            {
                Console.WriteLine(item);
            }
        }

        static void PrintStack()
        {
            // Method to print the stack collection
            foreach (var item in stack)
            {
                Console.WriteLine(item);
            }
        }

        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Collections Demo:\n");

            // Add to the dicitonary
            dict.Add("Apple", "Fruit");
            dict.Add("Carrot", "Vegetable");
            dict.Add("Potato", "Vegetable");
            dict.Add("Grape", "Fruit");
            dict.Add("Beetroot", "Vegetable");
            dict.Add("Artichoke", "Vegetable");
            dict.Add("Blueberry", "Fruit");
            dict.Add("Cherry", "Fruit");
            dict.Add("Lemon", "Fruit");
            dict.Add("Eggplant", "Vegetable");

            // Add to the queue
            queue.Enqueue("Apple");
            queue.Enqueue("Blueberry");
            queue.Enqueue("Cherry");
            queue.Enqueue("Grape");
            queue.Enqueue("Lemon");

            // Add to the stack
            stack.Push("Potato");
            stack.Push("Eggplant");
            stack.Push("Carrot");
            stack.Push("Beetroot");
            stack.Push("Artichoke");

            // Print collections after they're initialized
            Console.WriteLine("\nCollections (After Initialization):\n");

            Console.WriteLine("Dictionary contents:");
            PrintDictionary();

            Console.WriteLine("\nQueue contents:");
            PrintQueue();

            Console.WriteLine("\nStack contents:");
            PrintStack();

            // Remove the fruits from the dictionary
            dict.Remove("Apple");
            dict.Remove("Grape");
            dict.Remove("Blueberry");
            dict.Remove("Cherry");
            dict.Remove("Lemon");

            // Remove all but one item from the queue
            queue.Dequeue();
            queue.Dequeue();
            queue.Dequeue();
            queue.Dequeue();

            // Remove all but one item from the stack
            stack.Pop();
            stack.Pop();
            stack.Pop();
            stack.Pop();

            // Print collections after some items have been removed
            Console.WriteLine("\n\nCollections (After Removals):\n");

            Console.WriteLine("Dictionary contents:");
            PrintDictionary();

            Console.WriteLine("\nQueue contents:");
            PrintQueue();

            Console.WriteLine("\nStack contents:");
            PrintStack();
        }
    }
}
