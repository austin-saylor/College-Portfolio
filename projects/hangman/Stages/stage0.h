#include <iostream>
#include <string>

using namespace std;

// Creating strings to be used in all stages:
    const string gallow_top = "|-----------------";
    const string gallow_top2 = "|/        |";
    const string gallow_pole = "|";
    const string gallow_base = "===========";

void printStage0()
{
    cout << gallow_top << endl;
    cout << gallow_top2 << endl;
    cout << gallow_pole << endl;
    cout << gallow_pole << endl;
    cout << gallow_pole << endl;
    cout << gallow_pole << endl;
    cout << gallow_pole << endl;
    cout << gallow_base << endl;
    cout << "" << endl;
}