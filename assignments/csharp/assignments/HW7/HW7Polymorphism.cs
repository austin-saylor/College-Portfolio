using System;

namespace HW7
{
    public abstract class Vehicle
    {
        // Private variables (fields)
        private string make;
        private string model;
        private int year;
        private int price;

        // Constructor
        public Vehicle(string make, string model, int year, int price)
        {
            this.make = make;
            this.model = model;
            this.year = year;
            this.price = price;
        }

        // Getter/setter method for the 'make' variable
        public string Make
        {
            get { return make; }
            set { make = value; }
        }

        // Getter/setter for the 'model' variable
        public string Model
        {
            get { return model; }
            set { model = value; }
        }

        // Getter/setter method for the 'year' variable
        public int Year
        {
            get { return year; }
            set { year = value; }
        }

        // Getter/setter method for the 'price' variable
        public int Price
        {
            get { return price; }
            set { price = value; }
        }


        // Abstract methods to be overridden by derived classes
        public abstract void PrintMake();

        public abstract void PrintModel();

        public abstract void PrintYear();

        public abstract void PrintPrice();

        public abstract void DisplayInfo();
    }

    public class Car : Vehicle
    {
        // Constructor
        public Car(string make, string model, int year, int price) : base(make, model, year, price) 
        { 

        }

        // Override methods from the base class
        public override void PrintMake()
        {
            Console.WriteLine($"The make of the car is: {Make}.");
        }

        public override void PrintModel()
        {
            Console.WriteLine($"The model of the car is: {Model}.");
        }

        public override void PrintYear()
        {
            Console.WriteLine($"The year of the car is: {Year}.");
        }

        public override void PrintPrice()
        {
            Console.WriteLine($"The price of the car is: ${Price}.");
        }

        public override void DisplayInfo()
        {
            Console.WriteLine($"\nVehicle info: {Year} {Make} {Model}, priced at ${Price}.\n");
        }

        // Unique method for the 'Car' class - Summarizes the unique features of cars
        public void CarFeatures()
        {
            Console.WriteLine("Car Description:");
            Console.WriteLine($"The {Year} {Make} {Model} is a car, meaning that it is primarily intended for transporting passengers.");
            Console.WriteLine("Cars typically have a 'unibody' construction, meaning that it has a base frame and a body frame.");
            Console.WriteLine("This also means that cars could be safer for passengers.\n\n");
        }
    }

    public class Truck : Vehicle
    {
        // Constructor
        public Truck(string make, string model, int year, int price) : base(make, model, year, price) 
        { 

        }

        // Override methods from the base class
        public override void PrintMake()
        {
            Console.WriteLine($"The make of the truck is: {Make}.");
        }

        public override void PrintModel()
        {
            Console.WriteLine($"The model of the truck is: {Model}.");
        }

        public override void PrintYear()
        {
            Console.WriteLine($"The year of the truck is: {Year}.");
        }

        public override void PrintPrice()
        {
            Console.WriteLine($"The price of the truck is: ${Price}.");
        }

        public override void DisplayInfo()
        {
            Console.WriteLine($"\nVehicle info: {Year} {Make} {Model}, priced at ${Price}.\n");
        }

        // Unique method for the 'Truck' class - Summarizes the unique features of trucks
        public void TruckFeatures()
        {
            Console.WriteLine("Truck Description:");
            Console.WriteLine($"The {Year} {Make} {Model} is a truck, meaning that it is primarily intended for hauling and towing cargo.");
            Console.WriteLine("While cargo transport is the primary purpose of trucks, they are designed for passengers to some extent as well.");
            Console.WriteLine("Unlike cars, trucks have a 'body-on-frame' construction, which involves more components.");
            Console.WriteLine("'Body-on-frame' construction allows for greater flexibility when hauling cargo, and results");
            Console.WriteLine("in a heavier, bulkier vehicle.\n\n");
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Polymorphism: \n\n");

            // Create Car objects
            Car car1 = new Car("Toyota", "Camry", 2020, 20000);
            Car car2 = new Car("Tesla", "Model X", 2016, 60000);

            // Create Truck objects
            Truck truck1 = new Truck("Ford", "F-150", 2019, 70000);
            Truck truck2 = new Truck("Chevy", "Colorado", 2024, 30000);

            // Display info on each Car object
            Console.WriteLine("CARS:\n");
            car1.PrintMake();
            car1.PrintModel();
            car1.PrintYear();
            car1.PrintPrice();
            car1.DisplayInfo();
            car1.CarFeatures();

            car2.PrintMake();
            car2.PrintModel();
            car2.PrintYear();
            car2.PrintPrice();
            car2.DisplayInfo();
            car2.CarFeatures();

            // Display info on each Truck object
            Console.WriteLine("TRUCKS:\n");
            truck1.PrintMake();
            truck1.PrintModel();
            truck1.PrintYear();
            truck1.PrintPrice();
            truck1.DisplayInfo();
            truck1.TruckFeatures();

            truck2.PrintMake();
            truck2.PrintModel();
            truck2.PrintYear();
            truck2.PrintPrice();
            truck2.DisplayInfo();
            truck2.TruckFeatures();
        }
    }
}
