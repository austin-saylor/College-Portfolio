/*
Kattis - Module
Arrays Lab
Updated By: Austin Saylor
CSCI 111
Date: 11/11/22
Read and solve the Kattis problem: https://open.kattis.com/problems/modulo  
Algorithm Steps:
		1. Read 10 numbers into an array
		2. Create boolean array of size 42 to store the modulo 42 values (0-41)
      - initialize the array with false values
    3. For each of the 10 numbers:
      3.a find the modulo 42 and set the flag of the array at that index to true
    4. Go through the boolean array and count all true values
    5. Print the count of the true values to find the unique modulo 42 values
*/

#include <iostream>
#include <cassert>
using namespace std;

void readData(unsigned int *, size_t);
unsigned int getModulo42(const unsigned int);
void updateFlags(const unsigned int *, bool *, size_t);
size_t countFlags(bool * flags, size_t flag_len);
void initFlags(bool *, size_t);
void testGetModulo42();
void testCountFlags();

int main(int argc, char* argv[])
{

  size_t num_flags = 0;
  size_t flag_len = 42;

  if (argc == 2 and string(argv[1]) == string("test")) {
    // FIXME1 #fixed#: call testGetModulo42()
    testGetModulo42();
    // FIXME2 #fixed#: call testCountFlags()
    testCountFlags();
  }
  else {
    // create a dynamic unsigned int array of size 10 to store numbers
    unsigned int * nums = new unsigned int[10];
    // read 10 numbers into nums array
    readData(nums, 10); 
    // create a dynamic boolean array of size 42 to store module flags
    bool * flags = new bool[42];
    initFlags(flags, 42);
    updateFlags(nums, flags, 10);
    //FIXME #fixed# - call countFlags function passing proper argument and print the result
    num_flags = countFlags(flags, flag_len);
    cout << num_flags << endl;
  }
	return 0;
}

void readData(unsigned int * data, size_t arr_len) {
  for(int i=0; i<arr_len; i++) {
    cin >> data[i];
  }
}

void updateFlags(const unsigned int * numbers, bool * flags, size_t num_len) {
  unsigned int mod;
  for(int i=0; i<num_len; i++) {
    mod = getModulo42(numbers[i]);
    //cout << "mod = " << mod << endl;
    flags[mod] = true;
  }
}

unsigned int getModulo42(unsigned int num) {
  // FIXME #fixed#: return num modulo 42
  return num%42;
}

void initFlags(bool * flags, size_t flags_len) {
  for(int i=0; i<flags_len; i++) {
    flags[i] = false;
  }
}

size_t countFlags(bool * flags, size_t flag_len) {
  size_t count = 0;
  for (int i=0; i< flag_len; i++) {
    // FIXME #fixed#: if the flags at index i is set to true, increment count by 1
    if (flags[i] == true) {
      count += 1;
    }
  }
  return count;
}

void testGetModulo42() {
  assert(getModulo42(41) == 41);
  assert(getModulo42(42) == 0);
  assert(getModulo42(43) == 1);
  // FIXME #fixed#: Write 3 more test cases
  assert(getModulo42(44) == 2);
  assert(getModulo42(40) == 40);
  assert(getModulo42(39) == 39);
  cerr << "getModulo42(): All test cases passed!" << endl;
}

void testCountFlags() {
  bool * flags = new bool[42];
  initFlags(flags, 42);
  flags[getModulo42(42)] = true;
  flags[getModulo42(10)] = true;
  assert(countFlags(flags, 42) == 2);
  // reinitialize the flags array
  initFlags(flags, 42);
  flags[getModulo42(1)] = true;
  flags[420%42] = true;
  flags[43%42] = true;
  assert(countFlags(flags, 42) == 2);
  // FIXME #fixed#: write 3 more test cases
  assert(countFlags(flags, 10) == 1);
  assert(countFlags(flags, 8) == 3);
  assert(countFlags(flags, 5) == 6);
  cerr << "countFlags(): All test cases passed!" << endl;
}

void test() {
  testGetModulo42();
  testCountFlags();
}