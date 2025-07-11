/*
Austin Saylor
10/10/2022
CSCI 111

This program uses the number of contestants in a hypothetical contest, and the number of problems that they solved in this contest,
to determine how many carrots will be handed out as rewards.
*/
#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
    int contestants = 0;
    int problems_solved = 0;
    string description;
    
    cin >> contestants >> problems_solved;
    for(int i=0; i< contestants; i++)
    {
        cin >> description;
    }
    
    cout << problems_solved;

    return 0;
}