/*
Kattis - Dog & Gopher
Loop Lab
Updated By: Austin Saylor
CSCI 111
Date: 10/10/2022
Read and solve the Kattis problem: https://open.kattis.com/problems/doggopher 
Algorithm Steps:
		1. Read gopher and dog's coordinates
		2. Define a function to find and return the Euclidean distance between the two points
    3. For each gopher hole coordinate:
      3.a find the distance between the gopher position and the hole
      3.b find the distance between the dog position and the hole
      4.c if the dog's distance is larger or equal to twice the distance of gopher, 
          gopher can get away through that hole. 
          4.c.1 Stop testing other holes.
    4. If no safe hole is found, the gopher cannot escape.
*/

#include <iostream>
#include <cassert>
#include <string>
#include <iomanip>
#include <cmath>
#include <sstream>
using namespace std;

// Function prototypes
// Function finds the the Euclidean distance given two points (x1, y1) and (x2, y2)
double distance(const double x1, const double y1, const double x2, const double y2);
// function to test distance function
void testDistance();

#define TOLERANCE 1e-6 // 10^-6 or 0.000001

int main(int argc, char* argv[]) {
  if (argc == 2 and string(argv[1]) == string("test")) {
    // FIXME1: call testDistance function #fixed#
    testDistance();
  }
  else {
    double gopherX, gopherY;
    double dogX, dogY;
    double holeX, holeY; // varibles to read gopher hole coordinates
    string answer = "The gopher cannot escape.";
    double gopher_dist, dog_dist=0;
    // read gopher's coordinates
    cin >> gopherX >> gopherY;
    // FIXME2: read dog's coordinates #fixed#
    cin >> dogX >> dogY;
    while (cin >> holeX >> holeY) { // while there's hole coordinates to read
      // find gopher's distance from (x, y)
      gopher_dist = distance(gopherX, gopherY, holeX, holeY);
      // store the returned result into answer variable
      // FIXME3: find dog's distance from (x, y) #fixed#
      dog_dist = distance(dogX, dogY, holeX, holeY);
      if (dog_dist >= 2*gopher_dist) {
        ostringstream oss;
        oss << fixed << showpoint << setprecision(3);
        oss << "The gopher can escape through the hole at (" << holeX << "," << holeY << ").";
        answer = oss.str();
        break; // no need to test more holes; the first one will do!
      }
    }
    cout << answer << endl;
  }
	return 0;
}

// Function implementation
double distance(const double x1, const double y1, const double x2, const double y2) {
  // FIXME4: Find the Eucledian distance between two points on 2-d coordiantes. #fixed#
  double d = sqrt(pow((x2-x1), 2) + pow((y2-y1), 2));

  // store the distance into the `d` variable
	return d;
}

// function to test area function
void testDistance() {
  double x1, y1, x2, y2, answer, expected;
  x1 = 1.000f;
  y1 = 1.000f;
  x2 = 2.000f;
  y2 = 2.000f;
  answer = distance(x1, y1, x2, y2);
  expected = 1.4142135623731;
  cout << fixed << showpoint << setprecision(3) << endl;
  cout << answer << " " << expected << endl;
  assert(abs(answer-expected) < TOLERANCE);
  // FIXME5: Write 2nd test case for distance function #fixed#
  assert(distance(0, 0, 0, 100) == 100);
  // FIXME6: Write 3rd test case for distance function #fixed#
  assert(distance(0, 1, 1, 2) == sqrt(2));
  // FIXME7: Write 4th test case for distance function #fixed#
  assert(distance(-7, -4, 17, 64) == sqrt(5200));
  cerr << "All test cases passed!\n";
}