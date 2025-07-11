/*
Kattis - Seven Wonders
Updatd By: Austin Saylor
Date: 11/17/22
Read Seven Wonders Problem Statement: https://open.kattis.com/problems/sevenwonders
Algorithm steps:
1. Read cards into a string variable
2. use map<char, int> to keep track of count of each card played
  - update map: for each card, update its count
3. find regular points following the instruction
  - points = sum of (each card_count)^2
4. add bonus points if any
  - find # of sets of three cards and mulitiply it by 7 and add it to the total points
*/

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <map>
#include <string>

using namespace std;

using pos_int = unsigned int; // create type alias

pos_int points = 0;

// function prototypes
pos_int answer(const string& cards);
void testAnswer();
void solve();

int main(int argc, char* argv[]) {
    if (argc == 2 and string(argv[1]) == "test")
        testAnswer();
    else
        solve();
}

// solving the problem for kattis
void solve() {
    string cards;
    // string consists of only uppercase letters (no spaces) upto 50 chars
    // FIXME3 #fixed#
    // read std input into cards variable
    cin >> cards;
    cout << answer(cards) << endl;
}

pos_int answer(const string& cards) {
    // implment algorithm step 2
    // wonders is a map from char to int
    map<char, int> wonders;
    int count = 0;
    pos_int min_card = 999999;
    // for each card in cards
    for (char card: cards) {
      // check if card is already in wonders map
      auto find = wonders.find(card);
      if (find == wonders.end()) // card not found
        // add it to the wonders map
        wonders[card] = 1;
      else // FIXME4 #fixed#: update value of card 
      {
        wonders[card] += 1;
      }
    }
    // algorithm step 3 - calculate points
    //pos_int points = 0;
    for (auto pair: wonders) { // for is pair of <card, count>
      // FIXME5 #fixed# - Update the points by adding count^2
      points += pow(pair.second, 2);
      
      min_card = (pair.second < min_card)?pair.second:min_card;
    }
    // step 4 - add bonus points if any
    if (wonders.size() == 3) // if there are 3 unique cards
      points += min_card*7;

    return points;
}

// unit testing answer()
void testAnswer() {
    // FIXME6 #fixed#
    // write at least two test cases to test answer()
    string test_cards1 = "TTT";
    assert(answer(test_cards1) == 9);
    
    string test_cards2 = "TCCGGG";
    assert(answer(test_cards2) == 21);

    cerr << "All test cases passed!\n";
}