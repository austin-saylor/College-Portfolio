#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv) {

    int counter = 0;
    string str;

    for(int i = 0; i < 5; i++)
    {
        getline(cin,str);
        if( str.find("FBI") != string::npos )
        {
            cout << i+1 << " ";
            counter++;
        }
    }
    if( counter == 0 )
    {
        cout << "HE GOT AWAY!" << endl;
    }

    return 0;
}