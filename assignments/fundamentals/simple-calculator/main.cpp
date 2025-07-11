/*
Homework 3: Functions and Unit Testing
Name: Austin Saylor
Date: 10/3/2022
Program executes various mathematical operations, given two numbers, and outputs the corresponding value.
*/

#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>
#include <cmath>
 
using namespace std;
 
// function prints menu options
void printMenu(void);
 
// function prompts user to enter two numbers
// the numbers are stored in the parameters provided
void getTwoNumbers(double &, double &);
 
// function takes two numbers; finds and returns the sum of the two
double findSum(const double &, const double &);
 
// function takes two numbers; finds and returns the product of them
double findProduct(const double &, const double &);

// function takes two numbers; finds; returns the quotient of first divided by the second
double findQuotient(const double &, const double &);

// function takes two numbers; finds and returns the 2nd subtracted from the first
double findDifference(const double &, const double &);
 
// function takes two numbers; finds and returns the remainder
double findRemainder(const int &, const int &);
 
// function takes two numbers; finds and returns the first number, to the power of the second
double findPower(const double &, const double &);
 
// function takes one number; finds and returns the square root
double findSquareRoot(const double &, const double &);

// function takes two numbers; finds and returns the largest of the two
double findLarger(const double &, const double &);

// A function to validate each mathematical function 
void test();

// defines the function that runs the main program
bool program();

// function clears the screen using system call
// NOTE: system call is not a security best pracice!
void clearScreen() {
    // use "cls" in windows and "clear" command in Mac and Linux
    #ifdef _WIN32
        system("clS");
    #else
        system("clear");
    #endif
}

int main(int argc, char* argv[]) {
    bool keepRunning = true;
    if(argc == 2 && string(argv[1]) == "test") {
        test();
        exit(EXIT_SUCCESS); // exit the program
    }
    else {
        // A loop that keeps the program running, until the user chooses to quit.
        while (true) {
            if (!program()) // call program
                break; // break loop if program returned false
            cin.ignore(100, '\n');
            cout << "Press enter to continue.";
            cin.get();
            clearScreen();
        }
    }
    cin.ignore(100, '\n');
    cout << "Press enter to quit the program.\n";
    cout << "Goodbye!" << endl;
    return 0;
}

// A function that prints the menu of options
void printMenu(void) {
    cout << "Menu options:\n";
    cout << "[1] Add two numbers\n";
    cout << "[2] Multiply two numbers\n";
    cout << "[3] Find the quotient of two numbers\n";
    cout << "[4] Subtract two numbers\n";
    cout << "[5] Find the remainder of two numbers\n";
    cout << "[6] Calculate the first number, to the power of the second\n";
    cout << "[7] Square root a number\n";
    cout << "[8] Find the larger of two numbers\n";
    cout << "[9] Quit the program\n";
    cout << "Enter one of the menu options [1-9]: ";
}

// A function prompting the user for one number. Used in case 7
void getOneNumber(double &n1) {
    cout << "Please enter a number: ";
    cin >> n1;
}

// A function prompting the user for two numbers. Used in cases 1-6, 8
void getTwoNumbers(double &n1, double &n2) {
    cout << "Please enter two numbers, separated by a space: ";
    cin >> n1 >> n2;
}

// Function for Case 1:
double findSum(const double &n1, const double &n2) {
    return (n1 + n2); // Adding number 2 to number 1, and returning the result
}

// Function for Case 2:
double findProduct(const double &n1, const double &n2) {
    return (n1 * n2); // Multiplying number 1 by number 2, and returning the result
}

// Function for Case 3:
double findQuotient(const double &n1, const double &n2) {
    return (n1/n2); // Dividing number 1 by number 2, and returning the result
}

// Function for Case 4:
double findDifference(const double &n1, const double &n2) {
    return (n1 - n2); // Subtracting number 2 from number 1, and returning the result
}

// Function for Case 5:
double findRemainder(const int &n1, const int &n2) {
    double remainder = n1 % n2; // Finding the remainder of the two numbers
    return remainder; // Return the result
}

// Function for Case 6:
double findPower(const double &n1, const double &n2) {
    double power = pow(n1, n2); // Raising number 1 to the power of number 2
    return power; // Return the result
}

// Function for Case 7:
double findSquareRoot(const double &n1) {
    double square_root = sqrt(n1); // Taking the square root of the given number
    return square_root; // Returning the result
}   

// Function for Case 8:
double findLarger(const double &n1, const double &n2) {
    //find the larger of n1 and n2 and return it
    double larger = (n1 >= n2) ? n1 : n2; // Finding out which number is larger
    return larger; // Returning the result
}

// functions to run automated testing for various user-defined functions
void test() {
    // Test cases for findSum()
    assert(findSum(64, 512) == 576); // test case 1
    assert(findSum(-80, 256) == 176); // test case 2

    // Test cases for findProduct()
    assert(findProduct(50, 100) == 5000); // test case 1
    assert(findProduct(9, 9) == 81); // test case 2

    // Test cases for findQuotient()
    assert(findQuotient(1000, 10) == 100); // test case 1
    assert(findQuotient(1, 1000) == 0.001); // test case 2

    // Test cases for findDifference()
    assert(findDifference(100, 200) == -100); // test case 1
    assert(findDifference(-10, 50) == -60); // test case 2

    // Test cases for findRemainder()
    assert(findRemainder(100, 10) == 0); // test case 1
    assert(findRemainder(7, 2) == 1); // test case 2

    // Test cases for findPower()
    assert(findPower(10, 2) == 100); // test case 1
    assert(findPower(2, 10) == 1024); // test case 2

    // Test cases for findSquareRoot()
    assert (findSquareRoot(100) == 10); // test case 1
    assert (findSquareRoot(64) == 8); // test case 2

    // Test cases for findLarger()
    assert (findLarger(896, 10) == 896); // test case 1
    assert (findLarger(-74, 200) == 200); // test case 2

    printf("%s\n", "All test cases passed...");
}

// the crux of the program that uses all the defined functions
// the program is menu driven
bool program() {
    int option = 1; // variable to store user entered option
    double num1=0, num2=0; // variables to store two numbers entered by user
    // display menu options
    printMenu();
    // Input validation
    do {
        if (cin >> option && option >= 1 && option <= 9) {
            //input is valid, break loop
            break;
        }
        else {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Invalid option! please enter a value between 1 and 9" << endl;
        }
    } while (true);
            
    // Call the function(s) or perform some operations based on user input
    switch(option) {
        case 1:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findSum function; store the returned value in sum variable
            double sum = findSum(num1, num2);
            // display the result
            printf("The sum of %.2f & %.2f = %.2f\n", num1, num2, sum);
            break;
        }
        case 2:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findProduct function; store the returned value in product variable
            double product = findProduct(num1, num2);
            // display the result
            printf("The product of %.2f & %.2f is %.2f\n", num1, num2, product);
            break;
        }
        case 3:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findQuotient function; store the returned value in quotient variable
            double quotient = findQuotient(num1, num2);
            // display the result
            printf("The quotient of %.2f & %.2f is %.2f\n", num1, num2, quotient);
            break;
        }
        case 4:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findDifference function; store the returned value in diff variable
            double diff = findDifference(num1, num2);
            // display the result
            printf("The difference between %.2f & %.2f is %.2f\n", num1, num2, diff);
            break;
        }
        case 5:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findRemainder function; store the returned value in rem variable
            double rem = findRemainder(num1, num2);
            // display the result
            printf("The remainder of %.2f & %.2f is %.2f\n", num1, num2, rem);
            break;
        }
        case 6:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findPower function; store the returned value in power variable
            double power = findPower(num1, num2);
            // display the result
            printf("%.2f to the power of %.2f is %.2f\n", num1, num2, power);
            break;
        }
        case 7:
        {
            // get two numbers
            getOneNumber(num1);
            // call findSquareRoot function; store the returned value in square_root variable
            double square_root = findSquareRoot(num1);
            // display the result
            if ((num1) < 0) {
                cout << "** This is not a real number! **" << endl;
            }
            printf("The square root of %.2f is %.2f\n", num1, square_root);
            break;
        }
        case 8:
        {
            // get two numbers
            getTwoNumbers(num1, num2);
            // call findLarger function; store the returned value in larger variable
            double larger = findLarger(num1, num2);
            // display the result
            printf("The largest number between %.2f & %.2f is %.2f\n", num1, num2, larger);
            break;
        }
        case 9:
        {
        default: // must be option 9
            return false; // exit the program
        }
    }
    return true;
}