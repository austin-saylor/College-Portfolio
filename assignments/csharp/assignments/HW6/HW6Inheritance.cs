using System;

namespace HW6
{
    public class People
    {
        // Private variables (fields)
        private string name;

        // Constructor
        public People(string name)
        {
            this.name = name;
        }

        // Automatic getter/setter property
        public string Name
        {
            get { return this.name; }
            set { this.name = value; }
        }
    }

    public class Student : People
    {
        // Constructor
        public Student(string name) : base(name) 
        { 

        }

        // Print a statement saying that the current person is a student
        public void Describe()
        {
            Console.WriteLine($"{Name} is a student.");
        }
    }

    public class Teacher : People
    {
        // Constructor
        public Teacher(string name) : base(name) 
        { 

        }

        // Print a statement saying that the current person is a teacher
        public void Describe()
        {
            Console.WriteLine($"{Name} is a teacher.");
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Inheritance Demo: ");

            // Create various 'people' objects, specifically with the types 'Student' and 'Teacher'
            Student student = new Student("Shelbi");
            Teacher teacher = new Teacher("Jackson");

            // Label the proceeding names as being before the change
            Console.WriteLine("\n\nBefore name changing:\n");

            // Describe what 'group' of people each person is part of
            student.Describe();
            teacher.Describe();

            // Change the names of the student and teacher
            student.Name = "Austin";
            teacher.Name = "Jeremy";

            // Label the proceeding names as being before the change
            Console.WriteLine("\n\nAfter name changing:\n");

            // Describe what 'group' of people each person is part of
            student.Describe();
            teacher.Describe();
        }
    }
}
