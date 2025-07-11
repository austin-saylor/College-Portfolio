/*
Austin Saylor
10/10/2022
CSCI 111

This program asks the user for the input of a number, and then outputs whether or not that number is odd or even.
*/
#include <iostream>
using namespace std;

int main(){
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        int n;
        cin >> n;

        if (n % 2 == 0)
            cout << n << " is even";
        else
            cout << n << " is odd";
        cout << endl;
        
    }
    
    return 0;
}
