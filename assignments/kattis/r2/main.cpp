/*
Austin Saylor
10/10/2022
CSCI 111

This progam is given two values, with the second value being the mean of the first number and an unknown third number.
It finds the third number using this information.
*/

#include <iostream>

using namespace std;

double R1;
double S;

double R2 = 0;

// Function to restore R2
double restore(const double R1, const double S) {
    R2 = ((2*S) - R1);
    return R2;
}

int main() {

    // User input of R1 and S.
    cin >> R1;
    cin >> S;

    restore(R1, S);

    // Output R2
    cout << R2 << endl;

    return 0;
}