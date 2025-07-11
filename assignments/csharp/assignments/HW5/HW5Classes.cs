using System;

namespace HW5
{
    public class City
    {
        // Private variables (fields)
        private string name;
        private string country;
        private int population;

        // Constructor
        public City(string name, string country, int population)
        {
            this.name = name;
            this.country = country;
            this.population = population;
        }

        // Getter/Setter methods for 'name'
        public string GetName()
        {
            return name;
        }

        public void SetName(string newName)
        {
            name = newName;
        }

        // Getter/Setter methods for 'country'
        public string GetCountry()
        {
            return country;
        }

        public void SetCountry(string newCountry)
        {
            country = newCountry;
        }

        // Getter/Setter methods for 'population'
        public int GetPopulation()
        {
            return population;
        }

        public void SetPopulation(int newPopulation)
        {
            population = newPopulation;
        }

        // Method that displays info on the city
        public void DisplayCityInfo()
        {
            // Display information for the given city

            string city_name = GetName();
            string city_country = GetCountry();
            int city_pop = GetPopulation();

            Console.WriteLine($"City Information for {city_name}, {city_country}:");
            Console.WriteLine($"Name: {city_name}");
            Console.WriteLine($"Country: {city_country}");
            Console.WriteLine($"Population: {city_pop}");
            Console.WriteLine("\n");
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            // Create four objects of the 'City' class
            // The population figures represent the basic city population, NOT the metro area
            // Source: https://infocartography.com/world-top1000-pop
            City new_york = new City("New York", "United States", 8230290);
            City los_angeles = new City("Los Angeles", "United States", 3983540);
            City melbourne = new City("Melbourne", "Australia", 5061439);
            City sydney = new City("Sydney", "Australia", 4991654);

            // Display information for each city
            new_york.DisplayCityInfo();
            los_angeles.DisplayCityInfo();
            melbourne.DisplayCityInfo();
            sydney.DisplayCityInfo();

            // Modify the population of each city
            // (from standard city population to metro population)
            // Source: https://www.macrotrends.net/global-metrics/cities/largest-cities-by-population
            new_york.SetPopulation(19034000);
            los_angeles.SetPopulation(12598000);
            melbourne.SetPopulation(5316000);
            sydney.SetPopulation(5185000);

            // Notify the user of the update
            Console.WriteLine("NOTE: The population for each city will now be displayed in the form of the metro area population.\n\n");

            // Display updated information for each city
            new_york.DisplayCityInfo();
            los_angeles.DisplayCityInfo();
            melbourne.DisplayCityInfo();
            sydney.DisplayCityInfo();
        }
    }
}
