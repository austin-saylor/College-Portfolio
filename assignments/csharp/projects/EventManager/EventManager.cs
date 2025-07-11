using System;

namespace EventManager
{
    // Interface for Customer
    public interface ICustomer
    {
        string Name 
        { 
            // Getter method for 'Name'
            get; 
        }
        string Email 
        { 
            // Getter method for 'Email'
            get; 
        }
        string Phone 
        { 
            // Getter method for 'Phone'
            get; 
        }
    }

    // Interface for Order
    public interface IOrder
    {
        int OrderId 
        { 
            // Getter method for 'OrderID'
            get; 
        }
        ICustomer Customer 
        { 
            // Getter method for 'Customer'
            get; 
        }
    }

    // Customer class
    public class Customer : ICustomer
    {
        public string Name 
        { 
            // Getter/Setter method for 'Name'
            get; 
            set; 
        }
        public string Email 
        { 
            // Getter/Setter method for 'Email'
            get; 
            set; 
        }
        public string Phone 
        { 
            // Getter/Setter method for 'Phone'
            get;
            set; 
        }

        public Customer(string name, string email, string phone)
        {
            // Constructor
            Name = name;
            Email = email;
            Phone = phone;
        }
    }

    // Order class
    public class Order : IOrder
    {
        public int OrderId 
        { 
            // Getter/Setter method for 'OrderID'
            get;
            set; 
        }
        public ICustomer Customer
        { 
            // Getter/Setter method for Customer
            get; 
            set; 
        }

        // Define events
        public event EventHandler<OrderEventArgs> OrderPlaced;
        public event EventHandler<OrderEventArgs> OrderReadyToShip;

        public Order(int orderId, ICustomer customer)
        {
            // Constructor
            OrderId = orderId;
            Customer = customer;
        }

        public void PlaceOrder()
        {
            // Method to place orders
            OnOrderPlaced(new OrderEventArgs(this));
        }

        public void MarkReady()
        {
            // Method to mark order as ready to ship
            OnOrderReadyToShip(new OrderEventArgs(this));
        }

        public virtual void OnOrderPlaced(OrderEventArgs e)
        {
            // Method to trigger the order placed event
            OrderPlaced?.Invoke(this, e);
        }

        public virtual void OnOrderReadyToShip(OrderEventArgs e)
        {
            // Method to trigger the order ready event
            OrderReadyToShip?.Invoke(this, e);
        }
    }

    // Event arguments
    public class OrderEventArgs : EventArgs
    {
        public IOrder Order 
        { 
            // Getter method for 'Order'
            get; 
        }

        public OrderEventArgs(IOrder order)
        {
            Order = order;
        }
    }

    // Subscriber class
    public class OrderSubscriber
    {
        public async void OnOrderPlaced(object sender, OrderEventArgs e)
        {
            // Method to notify the system that the order has been placed
            Console.WriteLine($"\nOrder {e.Order.OrderId} for customer {e.Order.Customer.Name} has been placed.");

            // Process the order
            await ProcessOrder((Order)sender);
        }

        static async Task ProcessOrder(Order order)
        {
            // Method to notify the system that the order is being processed
            
            // Randomly determine a processing time for the order
            Random random = new Random();
            int processTime = random.Next(3000, 10001);

            // Notify the system that the order is being processed
            Console.WriteLine($"\nProcessing order {order.OrderId}...");

            // Wait for the given process time
            await Task.Delay(processTime);
            
            // Notify the system that the order has been processed
            Console.WriteLine($"\nOrder {order.OrderId} processing complete.");

            // Mark the order as ready to ship
            order.MarkReady();
        }

        public void OnOrderReadyToShip(object sender, OrderEventArgs e)
        {
            // Method to notify the subscriber that the order is ready to ship

            // Randomly determine a contact method for the current order
            Random random = new Random();
            int contactMethod = random.Next(1, 3);
            
            if (contactMethod == 1)
            {
                // If this order has the first contact method, notify the customer via email
                Console.WriteLine($"Sent to {e.Order.Customer.Email}: Your order, ID:{e.Order.OrderId}, is ready to ship!");
            } 
            else 
            {
                // If this order has the second (or any other contact method other than the first), notify the customer via phone
                Console.WriteLine($"Sent to {e.Order.Customer.Phone}: Your order, ID:{e.Order.OrderId}, is ready to ship!");
            }
        }
    }

    // Linq class to store LINQ methods 
    public class Linq
    {
        public static void CustomerNames(List<ICustomer> customers)
        {
            // LINQ method to display customer names
            var names = from customer in customers
                        orderby customer.Name
                        select customer.Name;
            Console.WriteLine("\tNames:\n\t\t" + string.Join("\n\t\t", names));
        }

        public static void CustomerEmails(List<ICustomer> customers)
        {
            // LINQ method to display customer emails
            var emails = from customer in customers
                         orderby customer.Name
                         select customer.Email;
            Console.WriteLine("\tEmails:\n\t\t" + string.Join("\n\t\t", emails));
        }

        public static void CustomerPhones(List<ICustomer> customers)
        {
            // LINQ method to display customer phone numbers
            var phones = from customer in customers
                         orderby customer.Name
                         select customer.Phone;
            Console.WriteLine("\tPhone Numbers:\n\t\t" + string.Join("\n\t\t", phones));
        }
    }

    public class EventManager
    {
        static async Task Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Welcome to the Order Management System!\n");

            // Create an instance of the subscriber class
            OrderSubscriber subscriber = new OrderSubscriber();

            // Create customers
            List<ICustomer> customers = new List<ICustomer>
            {
                new Customer("Austin Saylor", "austin@yalor.com", "(472) 586-9099"),
                new Customer("Bob Barley", "bob@barley.com", "(808) 804-1399"),
                new Customer("Charlie Peterson", "charlie@peterson.com", "(780) 411-3733"),
                new Customer("Jacob Johnson", "jake@johnny.com", "(707) 057-0845"),
                new Customer("Landon Lambert", "landon@lambert.com", "(104) 904-1035"),
                new Customer("Becky Thompson", "becky@tom.com", "(837) 597-8039"),
                new Customer("Shelbi Arthur", "shelbi@cows.com", "(583) 151-8478"),
                new Customer("Henry Peterson", "henry@pete.com", "(834) 499-3734"),
                new Customer("Isaac Englewood", "isaac@englewood.com", "(158) 873-4913"),
                new Customer("Emma Anderson", "emma@anderson.com", "(333) 884-9345")
            };

            // Create orders and attach event handlers
            List<Order> orders = new List<Order>();
            for (int i = 0; i < customers.Count; i++)
            {
                Order order = new Order(i + 1, customers[i]);
                order.OrderPlaced += subscriber.OnOrderPlaced;
                order.OrderReadyToShip += subscriber.OnOrderReadyToShip;
                orders.Add(order);
            }

            // Place orders
            orders[0].PlaceOrder();
            orders[1].PlaceOrder();
            orders[2].PlaceOrder();
            orders[3].PlaceOrder();
            orders[4].PlaceOrder();
            orders[5].PlaceOrder();
            orders[6].PlaceOrder();
            orders[7].PlaceOrder();
            orders[8].PlaceOrder();
            orders[9].PlaceOrder();

            // Wait for processing to complete
            await Task.Delay(11000);

            // LINQ queries to display customer Information
            Console.WriteLine("\n\nCustomer Information:");
            Linq.CustomerNames(customers);
            Linq.CustomerEmails(customers);
            Linq.CustomerPhones(customers);
        }
    }
}
