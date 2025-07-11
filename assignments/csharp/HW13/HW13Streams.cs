using System;
using System.IO;

namespace HW13
{
    public class HW13Streams
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Files and Streams Demo: \n");

            // Define the paths to the original and new files
            string originalFilePath = "files/original.txt";
            string newFilePath = "files/new.txt";

            // Write to the original file
            using (StreamWriter sw = new StreamWriter(originalFilePath))
            {
                sw.WriteLine("Hello, everyone!");
                sw.WriteLine("This is a message from me to you about how much I appreciate your work.");
                sw.WriteLine("Thank you for being the best coworkers that one can have.");
                sw.WriteLine("Sincerely, Austin.");
            }

            Console.WriteLine($"Original file created at '{originalFilePath}'");

            // Read the original file content
            string fileContent;
            using (StreamReader sr = new StreamReader(originalFilePath))
            {
                fileContent = sr.ReadToEnd();
            }

            // Manipulate the data using StringReader, and write it to the new file
            using (StringReader sr = new StringReader(fileContent))
            {
                using (StreamWriter sw = new StreamWriter(newFilePath))
                {
                    string? line;
                    do
                    {
                        // Manipulate the data (in this case, convert to uppercase)
                        line = sr.ReadLine();
                        string manipulatedLine = "";
                        if (line != null)
                        {
                            manipulatedLine = line.ToUpper();
                        }
                        sw.WriteLine(manipulatedLine);
                    } while (line != null);
                }
            }

            Console.WriteLine($"Manipulated file created at '{newFilePath}'");
        }
    }
}
