#include <iostream>

using namespace std;

int main(void)
{
    int a = 1, b = 1, c = 1;
    int x = 0, y = 0, z = 0;

    do
    {
        cin >> a >> b >> c;
        if(a == 0 || b == 0 || c == 0)
            return 0;
        if((a*a + b*b == c*c) || (a*a + c*c == b*b) || (b*b + c*c == a*a))
            cout << "right" << endl;
        else
            cout << "wrong" << endl;
    } while (true);
    
    return 0;
}