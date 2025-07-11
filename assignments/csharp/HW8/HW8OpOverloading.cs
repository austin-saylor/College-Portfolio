using System;

namespace HW8
{

    public class Fraction
    {
        private int numerator;
        private int denominator;

        public Fraction(int numerator, int denominator)
        {
            this.Numerator = numerator;
            this.Denominator = denominator;
        }

        private int Numerator
        {
            get { return this.numerator; }
            set { this.numerator = value; }
        }
        
        private int Denominator
        {
            get { return this.denominator; }
            set { this.denominator = value; }
        }

        public void PrintFraction()
        {
            Console.WriteLine($"{this.Numerator}/{this.Denominator}");
        }

        public override string ToString()
        {
            return $"{this.Numerator}/{this.Denominator}";
        }

        public static Fraction operator +(Fraction leftHandSide, Fraction rightHandSide)
        {
            int newNumerator, newDenominator;
            int product1, product2;

            Fraction newFrac = new Fraction(0, 0);
            
            if (leftHandSide.Denominator == rightHandSide.Denominator)
            {
                newNumerator = leftHandSide.Numerator + rightHandSide.Numerator;
                newFrac.Numerator = newNumerator;
                newFrac.Denominator = leftHandSide.Denominator;
                newFrac = Simplify(newFrac);
                return newFrac;
            }
            
            product1 = leftHandSide.Numerator * rightHandSide.Denominator;
            product2 = leftHandSide.Denominator * rightHandSide.Numerator;

            newNumerator = product1 + product2;
            newDenominator = leftHandSide.Denominator * rightHandSide.Denominator;

            newFrac.Numerator = newNumerator;
            newFrac.Denominator = newDenominator;
            newFrac = Simplify(newFrac);

            return newFrac;
        }

        public static Fraction operator *(Fraction leftHandSide, Fraction rightHandSide)
        {
            int newNumerator, newDenominator;

            Fraction newFrac = new Fraction(0, 0);

            newNumerator = leftHandSide.Numerator * rightHandSide.Numerator;
            newDenominator = leftHandSide.Denominator * rightHandSide.Denominator;

            newFrac.Numerator = newNumerator;
            newFrac.Denominator = newDenominator;
            newFrac = Simplify(newFrac);
            
            return newFrac;
        }

        public static Fraction operator /(Fraction leftHandSide, Fraction rightHandSide)
        {
            int newNumerator, newDenominator;
            int flippedNumerator, flippedDenominator;

            Fraction newFrac = new Fraction(0, 0);

            flippedNumerator = rightHandSide.Denominator;
            flippedDenominator = rightHandSide.Numerator;

            newNumerator = leftHandSide.Numerator * flippedNumerator;
            newDenominator = leftHandSide.Denominator * flippedDenominator;

            newFrac.Numerator = newNumerator;
            newFrac.Denominator = newDenominator;
            newFrac = Simplify(newFrac);
            
            return newFrac;
        }

        public static Fraction Simplify(Fraction inputFraction)
        {
            int greatestCommonDivisor;
            greatestCommonDivisor = GCD(inputFraction.Numerator, inputFraction.Denominator);

            return new Fraction(inputFraction.Numerator / greatestCommonDivisor,
                inputFraction.Denominator / greatestCommonDivisor);
        }
        private static int GCD(int a, int b)
        {
            if (b == 0)
            {
                return a;
            }

            return GCD(b, a % b);
        }

        public static bool operator ==(Fraction leftHandSide, Fraction rightHandSide)
        {
            if (leftHandSide.Numerator == rightHandSide.Numerator &&
                leftHandSide.Denominator == rightHandSide.Denominator)
            {
                return true;
            }

            return false;
        }
        
        public static bool operator !=(Fraction leftHandSide, Fraction rightHandSide)
        {
            return !(leftHandSide == rightHandSide);
        }
    }

    public class CSFractions
    {
        static void Main(string[] args)
        {
            // Start the program
            Console.WriteLine("Operator Overloading:\n");
            
            // Demonstrate addition
            Console.WriteLine("\nAddition Operator:\n");
            Fraction frac1 = new Fraction(3, 5);
            Fraction frac2 = new Fraction(1, 5);
            Console.WriteLine($"Fraction 1 = {frac1}");
            Console.WriteLine($"Fraction 2 = {frac2}\n");

            Fraction frac3 = frac1 + frac2;
            Console.WriteLine($"{frac1} + {frac2} equals...");
            frac3.PrintFraction();

            // Demonstrate Equality and Inequality
            Console.WriteLine("\n\nEquality and Inequality Operators:\n");
            Fraction frac4 = new Fraction(1, 3) + new Fraction(2, 6);
            Console.WriteLine("Fraction 4 equals...");
            frac4.PrintFraction();
            
            Console.WriteLine("\nFraction 1 == Fraction 2:");
            Console.WriteLine(frac1 == frac2); // False

            Console.WriteLine("\nFraction 3 != Fraction 4:");
            Console.WriteLine(frac3 != frac4); // True

            // Demonstrate Multiplication
            Console.WriteLine("\n\nMultiplication Operator:\n");
            Fraction frac5 = new Fraction(5, 8);
            Fraction frac6 = new Fraction(7, 11);
            Console.WriteLine($"Fraction 5 = {frac5}");
            Console.WriteLine($"Fraction 6 = {frac6}\n");

            Fraction frac7 = frac5 * frac6;
            Console.WriteLine($"{frac5} * {frac6} equals...");
            frac7.PrintFraction();

            // Demonstrate Division
            Console.WriteLine("\n\nDivision Operator:\n");
            Fraction frac8 = new Fraction(11, 7);
            Fraction frac9 = new Fraction(55, 66);
            Console.WriteLine($"Fraction 8 = {frac8}");
            Console.WriteLine($"Fraction 9 = {frac9}\n");

            Fraction frac10 = frac8 / frac9;
            Console.WriteLine($"({frac8}) / ({frac9}) equals...");
            frac10.PrintFraction();
        }
    }
}