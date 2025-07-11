#include <iostream>

using namespace std;

int main(void)
{
    string line = "";
    int count = 0;

    cin >> line;

    for(int i = 0; i < line.length(); i++)
    {
        if(i%3 == 0)
        {
            if(line[i] != 'P')
                count ++;
        }
        if(i%3 == 1)
        {
            if(line[i] != 'E')
                count ++;
        }
        if(i%3 == 2)
        {
            if(line[i] != 'R')
                count ++;
        }
    }

    cout << count;


    return 0;
}