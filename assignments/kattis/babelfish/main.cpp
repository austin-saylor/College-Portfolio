#include <iostream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

void test();

int main() {
    
    string input;
    string word;
    map <string, string> translation;

    while(true)
    {
        getline(cin, input);

        if(input == "")
        {
            break;
        } else {
            string home_word;
            string foreign_word;

            int i = 0;
            int size = input.size();
            int space = input.find(' ');

            home_word = input.substr(0, space);
            foreign_word = input.substr(space+1, size);

            translation.insert({foreign_word, home_word});
        }
    }

    while(true)
    {
        int i = -1;
        getline(cin, word);

        if (word == "")
        {
            break;
        } else {
            i += 1;
            int size = word.size();

            if (translation[word] != "")
            {
                cout << translation[word] << endl;
            } else {
                cout << "eh" << endl;
            }
        }
    }
}