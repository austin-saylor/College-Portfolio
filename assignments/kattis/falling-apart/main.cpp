#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

int main(void)
{
    int pieces;
    int alice_pot = 0;
    int bob_pot = 0;

    //cout << "Num pieces?" << endl;
    cin >> pieces;

    int * numbers = new int[pieces];

    for(int i = 0; i < pieces; i++)
    {
        cin >> numbers[i];
    }

    sort(numbers, (numbers+pieces));

    for(int i = (pieces - 1); i >= 0; i-=2)
    {
        if(i >= 0)
            alice_pot += numbers[i];
        //cout << numbers[i] << " ";
        if(i > 0)
            bob_pot += numbers[i-1];
           // cout << numbers[i-1] << endl;
    }

    cout << alice_pot << ' ' << bob_pot << endl;

    delete[] numbers;

    return 0;
}