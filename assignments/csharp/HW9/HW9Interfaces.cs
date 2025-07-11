using System;

namespace HW9
{
    interface IPlanet
    {
        // Setup methods for the 'IPlanet' interface.
        void Name();
        void Classification();
        void Distance();
    }

    public class Mars : IPlanet
    {
        // Define the 'IPlanet' methods in the context of Mars
        void IPlanet.Name()
        {
            Console.WriteLine("The name of the planet is 'Mars'.");
        }

        void IPlanet.Classification()
        {
            Console.WriteLine("The planet is classified as a Rocky Planet.");
        }

        void IPlanet.Distance()
        {
            Console.WriteLine("It is the 4th planet from the sun.");
        }
    }

    public class HW9Interfaces
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Interface Demo:\n");

            // Define an instance of IPlanet using Mars
            IPlanet mars = new Mars();

            // Call the methods of IPlanet using Mars
            mars.Name();
            mars.Classification();
            mars.Distance();
        }
    }
}
