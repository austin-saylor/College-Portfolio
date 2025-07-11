/*
Kattis - What does the fox say?
Arrays Lab
Updated By: Austin Saylor
CSCI 111
Date: 11/4/22
Read and solve the Kattis problem: https://open.kattis.com/problems/whatdoesthefoxsay   
Algorithm Steps:
	1. For each test case do the following:
    i. Read all the recorded sounds into a vector
    ii. Read individual animal sound until 'What does the fox say?' line
    iii. Replace all the matching sounds from the recorded sounds vecotor to "-"
    iv. Print the sounds that's left
*/

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cassert>

using namespace std;

void solve();
// function splits given string into vector of words
void splitString(vector<string> &, string);
// function 
void eraseAnimalSound(vector<string> &recordings, string sound);
void test_eraseAnimalSound();
void test_splitString();
string foxSays(vector<string> &);
void test_foxSays();
void unittest();

int main(int argc, char* argv[]) {
  if (argc == 2 and string(argv[1]) == string("test")) {
    // FIXME1 #fixed#: call unit test functions
    unittest();
  }
  // read the total number of test cases
  else
    solve();
  return 0;
}

void solve() {
  size_t T;
  cin >> T >> ws;
  
  while(T--) {
    //cout << "T = " << T << endl;
    vector<string> recordings;
    string sounds, animal_sound;
    getline(cin, sounds);
    //cout << sounds << endl;
    splitString(recordings, sounds);
    // read and parse animal sounds
    // don't know how many animals are there
    
    while (true) {
      getline(cin, animal_sound);
      // check for the question
      if (animal_sound == "what does the fox say?") break;
      istringstream iss(animal_sound);
      string animal, goes, sound;
      // parse three words
      iss >> animal >> goes >> sound;
      eraseAnimalSound(recordings, sound);
    }
    // FIXME2 #fixed#: call foxSays function and print the returned answer
    string fox_sound = foxSays(recordings);
    cout << fox_sound << endl;
  }
}

string foxSays(vector<string> &recordings) {
  // return the answer string
  ostringstream oss;
  bool first = true;
  for(int i=0; i<recordings.size(); i++) {
    if (recordings[i] == "-") continue;
    if (first) {
      oss << recordings[i];
      first = false;
    }
    else
      oss << " " << recordings[i];
  }
  return oss.str();
}

void splitString(vector<string> &words, string text) {
    string word;
    stringstream ss(text);
    while (ss >> word) {
        words.push_back(word);
    }
}

void eraseAnimalSound(vector<string> &recordings, string sound) {
  // for each sound s in recordings vector
  for (string & s: recordings) {
    // FIXME3 #fixed#: if s matches with sound, set it to '-'
    if (s == sound) {
        s = '-';
    }
  }
}

void test_splitString() {

  vector<string> answer;
  splitString(answer, "word");
  vector<string> actual = {"word"};
  assert(answer == actual);
  answer.clear();
  splitString(answer, "two word");
  vector<string> actual1 = {"two", "word"};
  assert(answer == actual1);

  // FIXME4 #fixed#: add 2 more test cases

  answer.clear();
  splitString(answer, "why is the fox's sound such a mystery?");
  vector<string> actual2 = {"why", "is", "the", "fox's", "sound", "such", "a", "mystery?"};
  assert(answer == actual2);
  cerr << "splitString(): All test cases passed!)\n";

  answer.clear();
  splitString(answer, "fox fox fox fox");
  vector<string> actual3 = {"fox", "fox", "fox", "fox"};
  assert(answer == actual3);
}

void test_foxSays() {

  vector<string> recordings = {"bo", "boo", "-", "ba", "-", "bo"};
  string ans = foxSays(recordings);
  assert(ans == "bo boo ba bo");

  // FIXME5 #fixed#: add 2 more test cases

  vector<string> recordings2 = {"smish", "smosh", "-", "bish", "-", "bosh"};
  string ans2 = foxSays(recordings2);
  assert(ans2 == "smish smosh bish bosh");

  vector<string> recordings3 = {"yip", "yip", "-", "yap", "-", "yip"};
  string ans3 = foxSays(recordings3);
  assert(ans3 == "yip yip yap yip");

  cerr << "foxSays(): All test cases passed!" << endl;
}

void test_eraseAnimalSound() {
  vector<string> recordings = {"bo", "boo", "meow", "ba", "wooon", "bo"};
  eraseAnimalSound(recordings, "bo");
  vector<string> expected = {"-", "boo", "meow", "ba", "wooon", "-"};
  assert(recordings == expected);

  // FIXME6 #fixed#: add 2 more test cases

  vector<string> recordings2 = {"toot", "woof", "wa", "ow", "pa", "blub"};
  eraseAnimalSound(recordings2, "ow");
  vector<string> expected2 = {"toot", "woof", "wa", "-", "pa", "blub"};
  assert(recordings2 == expected2);

  vector<string> recordings3 = {"ring", "ding", "ding", "ringa", "ding", "ding"};
  eraseAnimalSound(recordings3, "ringa");
  vector<string> expected3 = {"ring", "ding", "ding", "-", "ding", "ding"};
  assert(recordings3 == expected3);

  cerr << "eraseAnimalSound(): All test cases passed!" << endl;
}

void unittest() {
    test_splitString();
    test_foxSays();
    test_eraseAnimalSound();
}