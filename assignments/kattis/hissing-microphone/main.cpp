/*
Kattis - Hissing Microphone Problem
By: Austin Saylor
Date: 10/20/22
Hissing Microphone Problem Statement: https://open.kattis.com/problems/hissingmicrophone
Algorithm steps:
1. Read string
2. search for "ss" substring in the string
    - if found, print "hiss"
    - otherwise, print "no hiss"
*/

#include <iostream>
#include <string>
#include <cassert>

using namespace std;

// function prototypes
string answer(const string &line);
void testAnswer();
void solve();

int main(int argc, char* argv[]) {
    if (argc == 2 and string(argv[1]) == "test")
        testAnswer();
    else
        solve();
}

string answer(const string &line) {
    // FIXME3 #fixed#
    // implment algorithm step 2
    // return "hiss" if ss is found in line
    // otherwise, return "no hiss"
    std::string hiss = "ss";
    std::size_t found = line.find(hiss);
    if(found == std::string::npos)
        return "no hiss";
    else
        return "hiss";
}

// unit testing answer()
void testAnswer() {
    // FIXME4 #fixed#
    // write at least two test cases to test answer()
    string test1 = "Kentucky";
    string test2 = "Consistent";
    string test3 = "Kiss";

    assert(answer(test1) == "no hiss");
    assert(answer(test2) == "no hiss");
    assert(answer(test3) == "hiss");

    cerr << "All test cases passed!\n";
}

// solving the problem for kattis
void solve() {
    // string consists of only lowercase letters (no spaces) upto 30 chars
    string line;
    cin >> line;
    // FIXME5 #fixed#
    // read string into line
    cout << answer(line) << endl;
}