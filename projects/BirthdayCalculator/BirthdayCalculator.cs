using System;
using System.Collections.Generic;

namespace BirthdayCalc
{
    public class Birthdate
    {
        public static int[] Calculate_Age(int year, int month, int day)
        {
            DateTime birthDate = new DateTime(year, month, day);
            DateTime today = DateTime.Today;

            int years = today.Year - birthDate.Year;
            int months = today.Month - birthDate.Month;
            int days = today.Day - birthDate.Day;

            if (days < 0)
            {
                months--;
                days += DateTime.DaysInMonth(today.Year, today.Month - 1);
            }

            if (months < 0)
            {
                years--;
                months += 12;
            }

            int[] age = {years, months, days};
            return age;
        }

        public static int Validate_Age(int years)
        {
            if (years < 0)
            {
                // Invalid scenario: The user "hasn't" been born yet

                return -1;
            }

            if (years > 150)
            {
                // Invalid scenario: The user is older than what's possible
                //
                // The below link is to a Colorado State University article, explaining
                // research suggesting that the maximum possible age of a human is 150 years.
                // https://www.research.colostate.edu/healthyagingcenter/2022/10/07/humans-cant-live-forever/

                return -2;
            }

            // If the user's age is deemed valid, return 1.
            return 1;
        }

        public static string Conclude(int result, int years, int months, int days)
        {
            if (result == 1)
            {
                // If the result is valid, print the user's age
                string conclusion = $"\nYou are {years} years, {months} months, and {days} days old.";
                return conclusion;
            }
            else if (result == -1)
            {
                // If the user's entered birthday hasn't happened yet, explain it
                string conclusion = "\nSorry! This birthday is not possible. An individual with this birthday hasn't been born yet.";
                return conclusion;
            }
            else
            {
                // If the user's age is too old, explain it
                string error = "\nSorry! This birthday is not possible. ";
                string explanation = "This is age exceeds the maximum human life span!";

                string conclusion = error + explanation;
                return conclusion;
            }
        }

        public static bool Birthday(int year, int month, int day)
        {
            DateTime birthDate = new DateTime(year, month, day);
            DateTime today = DateTime.Today;

            // Check if it's the user's birthday today
            if (today.Month == birthDate.Month && today.Day == birthDate.Day)
            {
                // If it is the user's birthday, return true
                return true;
            }

            // If it isn't the user's birthday, return false
            return false;
        }
    }

    public class Astrology
    {
        private static readonly Dictionary<string, int[]> western_astrology = new Dictionary<string, int[]>()
        {
            { "Aquarius", new int[] {1, 20, 2, 18} },
            { "Pisces", new int[] {2, 19, 3, 20} },
            { "Aries", new int[] {3, 21, 4, 19} },
            { "Taurus", new int[] {4, 20, 5, 20} },
            { "Gemini", new int[] {5, 21, 6, 20} },
            { "Cancer", new int[] {6, 21, 7, 22} },
            { "Leo", new int[] {7, 23, 8, 22} },
            { "Virgo", new int[] {8, 23, 9, 22} },
            { "Libra", new int[] {9, 23, 10, 22} },
            { "Scorpio", new int[] {10, 23, 11, 21} },
            { "Sagittarius", new int[] {11, 22, 12, 21} },
            { "Capricorn", new int[] {12, 22, 1, 19} }
        };

        private static readonly Dictionary<string, int> chinese_astrology = new Dictionary<string, int>()
        {
            { "Monkey", 0 },
            { "Rooster", 1 },
            { "Dog", 2 },
            { "Pig", 3 },
            { "Rat", 4 },
            { "Ox", 5 },
            { "Tiger", 6 },
            { "Rabbit", 7 },
            { "Dragon", 8 },
            { "Snake", 9 },
            { "Horse", 10 },
            { "Goat", 11 }
        };

        private static bool InDateRange(DateTime date, DateTime startDate, DateTime endDate)
        {
            if (startDate <= endDate)
            {
                return date >= startDate && date <= endDate;
            }
            else
            {
                // Handles ranges that cross the year boundary (e.g., December 15 to January 10)
                return date >= startDate || date <= endDate;
            }
        }

        public static string Western_Sign(int month, int day)
        {
            DateTime date = new DateTime(DateTime.Now.Year, month, day); // Year is current year

            foreach (var sign in western_astrology)
            {
                var startDate = new DateTime(DateTime.Now.Year, sign.Value[0], sign.Value[1]);
                var endDate = new DateTime(DateTime.Now.Year, sign.Value[2], sign.Value[3]);

                if (InDateRange(date, startDate, endDate))
                {
                    return sign.Key;
                }
            }

            return "Unknown";
        }

        public static string Chinese_Sign(int year)
        {
            int key = year % 12;
            foreach (var sign in chinese_astrology)
            {
                if (sign.Value == key)
                {
                    return sign.Key;
                }
            }

            return "Unknown";
        }
    }

    public class BirthdayCalculator
    {
        static void Main(string[] args)
        {
            // Print the opening message
            Console.WriteLine("\nWelcome to the Birthday Calculator!\n");

            bool valid_date = false;
            while (!valid_date)
            {
                try
                {
                    // Have the user enter their birthday with their birth year, month, and day
                    Console.Write("\nPlease enter your birth year: ");
                    int year = int.Parse(Console.ReadLine());

                    Console.Write("Please enter your birth month: ");
                    int month = int.Parse(Console.ReadLine());

                    Console.Write("Please enter your birth day: ");
                    int day = int.Parse(Console.ReadLine());

                    // Calculate the user's age
                    int[] age = Birthdate.Calculate_Age(year, month, day);

                    // Separate the components of the user's age, and see if it's valid
                    int years = age[0];
                    int months = age[1];
                    int days = age[2];

                    int result = Birthdate.Validate_Age(years);

                    // Form a conclusion about the age, based on its validity, then print it
                    string conclusion = Birthdate.Conclude(result, years, months, days);
                    Console.WriteLine(conclusion);

                    // If the birthday is valid:
                    if (result == 1)
                    {
                        // Check if it's the user's birthday
                        bool birthday = Birthdate.Birthday(year, month, day);

                        if (birthday)
                        {
                            // If it is the user's birthday, wish them a happy birthday
                            string birthday_msg = "Happy Birthday!!!";
                            Console.WriteLine(birthday_msg);
                        }

                        // Compute the user's astrological info
                        string western_sign = Astrology.Western_Sign(month, day);
                        string chinese_sign = Astrology.Chinese_Sign(year);

                        // Print the user's astrological info
                        Console.WriteLine("\nHere's your astrological information: ");
                        Console.WriteLine($"Western Zodiac Sign: {western_sign}");
                        Console.WriteLine($"Chinese Zodiac Sign: {chinese_sign}");

                        // End the loop
                        valid_date = true;
                    }
                }
                catch (Exception ex)
                {
                    // If the provided date doesn't exist,
                    // send an error and allow them to try again
                    Console.WriteLine("ERROR: Invalid date! Please try again.\n");
                }
            }
        }
    }
}
