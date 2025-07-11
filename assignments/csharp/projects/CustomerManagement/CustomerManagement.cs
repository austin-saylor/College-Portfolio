using System;
using System.Collections.Generic;
using System.IO;

namespace CustomerMgmt
{
    // Define the ICustomer interface
    public interface ICustomer
    {
        string GetLastName();
        string GetFirstName();
        string GetID();
        string GetBusiness();
        string GetPhone();
    }

    // Define the customer object (class)
    public class Customer : ICustomer, IComparable<Customer>
    {
        // Private variables (fields)
        private string lastName;
        private string firstName;
        private int customerID;
        private string businessName;
        private string phoneNumber;

        // Constructor
        public Customer(string lastName, string firstName, int customerID, string businessName, string phoneNumber)
        {
            this.lastName = lastName;
            this.firstName = firstName;
            this.customerID = customerID;
            this.businessName = businessName;
            this.phoneNumber = phoneNumber;
        }

        // Automatic getter/setter property for 'lastName'
        public string LastName
        {
            get { return this.lastName; }
            set { this.lastName = value; }
        }

        // Automatic getter/setter property for 'firstName'
        public string FirstName
        {
            get { return this.firstName; }
            set { this.firstName = value; }
        }

        // Automatic getter/setter property for 'customerID'
        public int CustomerID
        {
            get { return this.customerID; }
            set { this.customerID = value; }
        }

        // Automatic getter/setter property for 'businessName'
        public string BusinessName
        {
            get { return this.businessName; }
            set { this.businessName = value; }
        }

        // Automatic getter/setter property for 'phoneNumber'
        public string PhoneNumber
        {
            get { return this.phoneNumber; }
            set { this.phoneNumber = value; }
        }

        // Implement 'GetLastName' method from the ICustomer interface
        public string GetLastName()
        {
            return $"Last Name: {LastName}\n";
        }

        // Implement 'GetFirstName' method from the ICustomer interface
        public string GetFirstName()
        {
            return $"First Name: {FirstName}\n";
        }

        // Implement 'GetID' method from the ICustomer interface
        public string GetID()
        {
            return $"ID: {CustomerID}\n";
        }

        // Implement 'GetBusiness' method from the ICustomer interface
        public string GetBusiness()
        {
            return $"Business: {BusinessName}\n";
        }

        // Implement 'GetPhone' method from the ICustomer interface
        public string GetPhone()
        {
            return $"Phone: {PhoneNumber}";
        }

        // Override the ToString method
        public override string ToString()
        {
            // Format the customer data into a string
            string lName = GetLastName();
            string fName = GetFirstName();
            string id = GetID();
            string business = GetBusiness();
            string phone = GetPhone();
            return $"{lName}{fName}{id}{business}{phone}";
        }

        // Implement the CompareTo method from IComparable<Customer>
        public int CompareTo(Customer other)
        {
            if (other == null)
                return 1;

            return this.customerID.CompareTo(other.customerID);
        }
    }

    public class CustomerManagement
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Organizing customer data...");

            // Create the paths to the input and output files
            string filePath = "files/entries.txt";
            string outputFilePath = "files/customers.txt";

            // Define a list of customers
            List<Customer> customers = new List<Customer>();

            // Ensure that the file path exists
            if (!File.Exists(filePath))
            {
                Console.WriteLine($"File {filePath} does not exist.");
                return;
            }

            // Read from the entry file, and add the info to the list of customers
            using (StreamReader sr = new StreamReader(filePath))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    List<string> customerInfo = new List<string>(line.Split(new string[] { ", " }, StringSplitOptions.None));
                    if (customerInfo.Count == 5)
                    {
                        Customer newCustomer = new Customer(customerInfo[0], customerInfo[1], int.Parse(customerInfo[2]), customerInfo[3], customerInfo[4]);

                        // Check for duplicate customer IDs
                        bool isDuplicate = false;
                        foreach (var customer in customers)
                        {
                            if (newCustomer.CompareTo(customer) == 0)
                            {
                                // If the ID is a duplicate of an existing one, skip adding it
                                isDuplicate = true;
                                break;
                            }
                        }

                        if (!isDuplicate)
                        {
                            // If it is not a duplicate ID, proceed with adding it to the list
                            customers.Add(newCustomer);
                        }
                    }
                }
            }

            // Write the organized customer data into the customers file
            using (StreamWriter sw = new StreamWriter(outputFilePath))
            {
                foreach (var customer in customers)
                {
                    sw.WriteLine(customer.ToString());
                    sw.WriteLine(); // Write an empty line
                }
            }

            // End the program with a finish statement
            Console.WriteLine($"All customer data has been organized! It has been written to '{outputFilePath}'");
        }
    }
}
