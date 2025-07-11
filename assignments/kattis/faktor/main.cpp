/*
Austin Saylor
10/10/2022
CSCI 111
*/

#include <iostream>

using namespace std;

int main() {
    int a, i;

    // Prompting user for the number of articles, and the impact factor
    cin >> a >> i;

    int ans = a * (i-1);

    // Outputing the number of scientists that need to be bribed
    cout << ans + 1 << endl;
}