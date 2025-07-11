#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <cassert>

using namespace std;

using big_int = long long int;

//function that reads numbers
//void readData(string, int);
void readStuff(string *, int);
//function that prints each element in the array
void printArray(string *, int);
// crux of the program is done in this function
void program();
// A function to unit test
void test();

int main(int argc, char* argv[]) {
	program();
	return 0;
}

// crux of the program
void program() {
	int N;

    cin >> N;
	cin.ignore(10000, '\n');

    string inputs[N]; //declare a dynamic int array of size 
    readStuff(inputs, N); //read the data into nums array
}

//read data from a file and store it in into given nums array.
void readStuff(string names[], int size)
{
	string line = "";
	int updown = 0;

	
	for( int i=0; i < size; i++)
	{
		getline(cin, line);
		names[i] = line;
	}

	for(int i = 1; i < size; i++)
	{
		if(names[i] > names[i-1])
		{
			updown += 1;
		}
		else if(names[i] < names[i-1])
		{
			updown -= 1;
		}
		else {
			//updown = 0;
			//cout << "Equal so far" << endl;
		}
	}
	if(updown == size-1)
	{
		cout << "INCREASING" << endl;
	}
	else if(updown == -(size-1))
	{
		cout << "DECREASING" << endl;
	}
	else
	{
		cout << "NEITHER" << endl;
	}
	
}

void Aswap(int &n1, int &n2)
{
    int a = n2;
    n2 = n1;
    n1 = a;
}