/*
Austin Saylor
10/10/2022
CSCI 111

This program asks the user to input numbers, and then outputs how much of those numbers were below 0.
*/
#include <iostream>

using namespace std;

int answer(void);

int main(void)
{
    int ans = 0;
    int num = 0;

    ans = answer();
    cout << ans << endl;

    return 0;
}

int answer(void)
{
    int sum = 0;
    int num = 0;
    int temp = 0;    
    
    cin >> num;

    for (int i=0; i<num;i++)
    {
        cin >> temp;
        if (temp < 0)
            sum ++;
    }
    
    return sum;
}