#include <iostream>
#include <string>
#include <map>
#include <cassert>

using namespace std;

int main() {
    
    map<char, string> Translator = {{'A', "@"}, {'B', "8"}, {'C', "("}, {'D', "|)"}, {'E', "3"}, {'F', "#"}, {'G', "6"}, {'H', "[-]"},
                                    {'I', "|"}, {'J', "_|"}, {'K', "|<"}, {'L', "1"}, {'M', "[]\\/[]"}, {'N', "[]\\[]"}, {'O', "0"},
                                    {'P', "|D"}, {'Q', "(,)"}, {'R', "|Z"}, {'S', "$"}, {'T', "']['"}, {'U', "|_|"}, {'V', "\\/"},
                                    {'W', "\\/\\/"}, {'X', "}{"}, {'Y', "`/"}, {'Z', "2"}, {'a', "@"}, {'b', "8"}, {'c', "("}, 
                                    {'d', "|)"}, {'e', "3"}, {'f', "#"}, {'g', "6"}, {'h', "[-]"}, {'i', "|"}, {'j', "_|"}, {'k', "|<"}, 
                                    {'l', "1"}, {'m', "[]\\/[]"}, {'n', "[]\\[]"}, {'o', "0"}, {'p', "|D"}, {'q', "(,)"}, {'r', "|Z"}, 
                                    {'s', "$"}, {'t', "']['"}, {'u', "|_|"}, {'v', "\\/"}, {'w', "\\/\\/"}, {'x', "}{"}, {'y', "`/"}, 
                                    {'z', "2"}};

    string input;
    getline(cin, input);

    int size = input.size();

    for (int i = 0; i < size; i++) {
        char c = tolower(input[i]);

        if ((c >= 'a' and c <= 'z'))
            cout << Translator[input[i]];
        else
            cout << input[i];
    }
}