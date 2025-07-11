/*
Kattis - Simon Says
By: Austin Saylor
Date: 10/21/22
Problem Statement: https://open.kattis.com/problems/simonsays 
Algorithm steps:
1. Read N
2. Loop N times:
  i. Read a line
  ii. If the line starts with "Simon says",
    print the rest of the string. Note: print the leading space after says as well!
  iii. Otherwise, skip the line.
*/

#include <iostream>
#include <string>
#include <cassert>

using namespace std;

// function prototypes
string answer(const string &line);
void testAnswer();
void solve();

string answer(const string &line) {
  // FIXME2: If the line starts with "Simon says", return rest of the line after says
  // including the space after says, otherwise return empty string ""
  // Hint: use find method on line object
  string simon = "Simon says";
  size_t found = line.find(simon);
  string phrase;

  if (line.find(simon) != string::npos) {
  //(line.find(simon) == 0) {
    phrase = line.substr(10, 90);
  } else {
    phrase = "";
  }
  return phrase;
}

// unit testing answer()
void testAnswer() {
  cout << "This is inside the testAnswer function" << endl;
  string ans = answer("Simon says laugh!");
  // let's double check what the returned answer is
  cerr << "ans = " << ans << endl;
  cout << ans << endl;
  assert(ans == " laugh!"); 
  assert(answer("Write more programs.") == "");
  // FIXME3 #fixed#: write at least two test cases to test answer()
  assert(answer("Simon says sit down.") == " sit down.");
  assert(answer("Sullivan says stand up!") == "");
  cerr << "All test cases passed!\n";
}

// solving the problem for kattis
void solve() {
  string ans;
  string line;
  int N;
  cin >> N;
  //FIXME4 : read and discard \n left behind
  cin.ignore(1000, '\n');
  while (N--) {
    //Note: string consists of phrase with spaces
    //FIXME5: read the whole line into line
    getline(cin, line);
    //FIXME6: call answer function and store the returned value into ans
    ans = answer(line);
    //FIXME7: print ans
    cout << ans << endl;
    if (ans == "") continue;
  }
}

int main(int argc, char* argv[]) {
  if (argc == 2 and string(argv[1]) == "test") {
    //FIXME1 #fixed#: call testAnswer function
    testAnswer();
  }
  else
    solve();
}