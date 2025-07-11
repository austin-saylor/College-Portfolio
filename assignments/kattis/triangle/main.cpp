/*
Kattis - Triangle Area problem
Function and Unit Testing
Updated By: Austin Saylor
CSCI 111
Date: 10/1/2022
Read and solve Triangle Area problem: https://open.kattis.com/problems/triarea 
Algorithm:
		1. Read height and base of a right triangle
		2. Define a function to find and return area given height and base of a right triangle
      2.a Area is given by the equation: (Base * Height)/2
    3. Call the function to print the result
    4. Write a test function to test the area function implemented in step 2
*/

#include <iostream>
#include <cstdio>
#include <cassert> //assert function
#include <string>
using namespace std;

// Function prototypes
// Function finds the area of the triangle
double areaOfTriangle(double height, double base);
// function to test area function
void testArea();

#define MAX_ERROR 1e-7 // 10^-7 or 0.0000007

void clearScreen() {
    // use "cls" in windows and "clear" command in Mac and Linux
    #ifdef _WIN32
        system("clS");
    #else
        system("clear");
    #endif
}

// function to test area function
void testArea() {
  int height, base;
  float answer, expected;
  height = 10;
  base = 5;
  answer = areaOfTriangle(height, base);
  expected = 25.0;
  assert(abs(answer-expected) < MAX_ERROR);
  // FIXME3: Write 2nd test case #fixed#
  assert((areaOfTriangle(5, 10)) == 25);
  // FIXME4: Write 3rd test case #fixed#
  assert((areaOfTriangle(512, 36)) == 9216);
  // FIXME5: Write 4th test case #fixed#
  assert((areaOfTriangle(16, 16)) == 128);
  assert((areaOfTriangle(1, 1)) == 0.5);
}

// Function implementation
double areaOfTriangle(double height, double base) {
  // FIXME2: Find the area of traingle using the formula given in algorithm step: 2.a #fixed#
  // store the area into area variable
  double area = ((base * height)/2);
	return area;
} 

int main()
{
  int base, height;

  {
    clearScreen();
    // parse the input stream
    cin >> base;

    // parse the input stream
    cin >> height;

    // call testArea function
    testArea();
	  // FIXME1: Call area function passing proper arguments #fixed#
    areaOfTriangle(height, base);
	  // print answer
    double answer = areaOfTriangle(height, base);
	  printf("%.1f", answer);
	  return 0;
  }
}