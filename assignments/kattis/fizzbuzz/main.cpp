#include <iostream>

using namespace std;

int x, y, n;
int a = 1;

void FizzBuzz() {

    cin >> x >> y >> n;

    while(a <= n) {
        if (a % x == 0 && a % y == 0) {
            cout << "FizzBuzz" << endl;
        }
        else if (a % x == 0) {
            cout << "Fizz" << endl;
        }
        else if (a % y == 0) {
            cout << "Buzz" << endl;
        }
        else {
            cout << a << endl;
        }
        a += 1;
    }
}

int main() {
    FizzBuzz();
    return 0;
}