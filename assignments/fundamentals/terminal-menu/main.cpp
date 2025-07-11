/*
Homework 4: CLI Menu
Name: Austin Saylor
Date: 11/7/2022
This program asks the user for a series of five numbers, and then analyzes a few characteristics about this series of numbers.
*/

#include <iostream>
#include <cstdio>
#include <string>
#include <cassert>
#include <cmath>
 
using namespace std;

double num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0; // variables to store five numbers entered by user
string name; // A variable to store the user's name
int cq = 0;
 
// function prints menu options
void printMenu(void);
 
// function prompts user to enter five numbers
// the numbers are stored in the parameters provided
void getFiveNumbers(double &, double &, double &, double &, double &);

// function takes five numbers; finds and returns the largest of the five
double findLarger(const double &, const double &, const double &, const double &, const double &);

// function takes five numbers; finds and returns the smallest of the five
double findSmaller(const double &, const double &, const double &, const double &, const double &);
 
// function takes five numbers, finds the sum of them, rounds it down, and then states whether it's odd, even, or equal to zero.
string analyzeFloorOfSum(const double &, const double &, const double &, const double &, const double &);

// A function to validate the other functions 
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
            cout << "Hi there! What is your name?" << endl;
            cin >> name;

            cout << "Hi, " + name + "!" << endl;
            getFiveNumbers(num1, num2, num3, num4, num5);

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
    cout << "[1] Find the largest of the five numbers\n";
    cout << "[2] Find the smallest of the five numbers\n";
    cout << "[3] Determine if the floor of the sum is odd, even, or zero\n";
    cout << "[4] Quit the program\n";
    cout << "Enter one of the menu options [1-4]: ";
}

// A function prompting the user for five numbers.
void getFiveNumbers(double &n1, double &n2, double &n3, double &n4, double &n5) {
    cout << "Please enter five numbers, separated by a space: ";
    cin >> n1 >> n2 >> n3 >> n4 >> n5;
}

// Function for Case 1:
double findLarger(const double &n1, const double &n2, const double &n3, const double &n4, const double &n5) {
    //find the larger of n1 and n2 and return it
    double larger; // Finding out which number is larger
    if (n1 > n2 && n1 > n3 && n1 > n4 && n1 > n5) {
        larger = n1;
    } else if (n2 > n1 && n2 > n3 && n2 > n4 && n2 > n5) {
        larger = n2;
    } else if (n3 > n1 && n3 > n2 && n3 > n4 && n3 > n5) {
        larger = n3;
    } else if (n4 > n1 && n4 > n2 && n4 > n3 && n4 > n5) {
        larger = n4;
    } else {
        larger = n5;
    }
    return larger; // Returning the result
}

// Function for Case 2:
double findSmaller(const double &n1, const double &n2, const double &n3, const double &n4, const double &n5) {
    //find the smaller of n1 and n2 and return it
    double smaller; // Finding out which number is smaller
    if (n1 < n2 && n1 < n3 && n1 < n4 && n1 < n5) {
        smaller = n1;
    } else if (n2 < n1 && n2 < n3 && n2 < n4 && n2 < n5) {
        smaller = n2;
    } else if (n3 < n1 && n3 < n2 && n3 < n4 && n3 < n5) {
        smaller = n3;
    } else if (n4 < n1 && n4 < n2 && n4 < n3 && n4 < n5) {
        smaller = n4;
    } else {
        smaller = n5;
    }
    return smaller; // Returning the result
}

// Function for Case 3:
string analyzeFloorOfSum(const double &n1, const double &n2, const double &n3, const double &n4, const double &n5) {

    double sum = n1 + n2 + n3 + n4 + n5; // Finding the sum of the five numbers
    int floor_sum = floor(sum); // Finding the floor of this sum
    string conclusion; // A variable to store the conclusion

    if (floor_sum == 0) {
        conclusion = "The floor of the sum of these numbers is equal to zero.";
    } else if (floor_sum % 2 == 0) {
        conclusion = "The floor of the sum of these numbers is even.";
    } else {
        conclusion = "The floor of the sum of these numbers is odd.";
    }

    return conclusion; // Returning the conclusion
}

// functions to run automated testing for various user-defined functions
void test() {
    // Test cases for analyzeFloorOfSum()
        // Test Case 1:
            string ans = analyzeFloorOfSum(-543, 973, 943, -156, -813);
            assert(ans == "The floor of the sum of these numbers is even.");
        // Test Case 2:
            string ans2 = analyzeFloorOfSum(442, 828, 119, -186, -563);
            assert(ans2 == "The floor of the sum of these numbers is even.");
        // Test Case 3:
            string ans3 = analyzeFloorOfSum(283, -902, 726, 967, -873);
            assert(ans3 == "The floor of the sum of these numbers is odd.");

    // Test cases for findLarger()
        assert(findLarger(1, 3, 5, 7, 9) == 9); // Test Case 1
        assert(findLarger(-197, 1024, 4096, -2556, 999999999) == 999999999); // Test Case 2
        assert(findLarger(-87, -1000000, -8750, -256, 1) == 1); // Test Case 3

    // Test cases for findSmaller()
        assert(findSmaller(896, 10, 957, 274, 112) == 10); // Test Case 1
        assert(findSmaller(-74, 200, -829, -267, -735) == -829); // Test Case 2
        assert(findSmaller(-300, 470, -556, -895, -997) == -997); // Test Case 3

    printf("%s\n", "All test cases passed...");
}

// the crux of the program that uses all the defined functions
// the program is menu driven
bool program() {
    int option = 1; // variable to store user entered option

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
            // call findLarger function; store the returned value in sum variable
            double larger = findLarger(num1, num2, num3, num4, num5);
            // display the result
            printf("The largest of the numbers is %.2f\n", larger);
            break;
        }
        case 2:
        {
            // call findSmaller function; store the returned value in sum variable
            double smaller = findSmaller(num1, num2, num3, num4, num5);
            // display the result
            printf("The smallest of the numbers is %.2f\n", smaller);
            break;
        }
        case 3:
        {
            // call analyzeFloorOfSum function; store the returned value in sum variable
            string analysis = analyzeFloorOfSum(num1, num2, num3, num4, num5);
            // display the result
            cout << analysis << endl;
            break;
        }
        case 4:
        {
        default: // must be option 4
            return false; // exit the program
        }
    }
    return true;
}