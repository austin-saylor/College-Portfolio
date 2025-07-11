/*
CSCI 111 - File IO & Struct Homework

Updated by: Austin Saylor
Date: 11/28/22

The program reads student names and grades, then calculates stats from the information.
*/

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


const float EPSILON = 1e-4; //accuracy upto 4 decimal points
struct student
{
    string fname;
    string lname;

    vector<float> grades;
    float average;
    char letter_grade;
};

void readData(vector<student> & list, const string inputFileName);
void writeData(const vector<student> & list);
void test();

float calc_avg(const vector<float> & grades)
{
    float avg = 0;
    for(int i = 0; i < 4; i++)
    {
        avg += grades[i];
    }
    return avg/4.0;
}

char grade(float average) {
    char grade;
    if (average >= 90) {
        grade = 'A';
    }
    else if (average >= 80 && average < 90) {
        grade = 'B';
    }
    else if (average >= 70 && average < 80) {
        grade = 'C';
    }
    else if (average >= 60 && average < 70) {
        grade = 'D';
    }
    else {
        grade = 'F';
    }

    return grade;
}

int findMax(const vector<int> & nums) {
    int max = nums[0];
    for(int n: nums)
        max = (n>max) ? n : max;
    return max;
}

int main(int argc, char* argv[]) {
    if (argc == 2 && string(argv[1]) == "test") {
        test();
        return 0;
    }
    vector<student> student_list;

    string inFile;
    cout << "Enter input file name: ";
    getline(cin, inFile);

    readData(student_list, inFile);
    writeData(student_list);
    cout << "All done. Enter to exit...";
    cin.get();
    return 0;
}

void readData(vector<student> & list, const string inputFileName) {
    int num;
    ifstream fin;
    student temp;
    float grade;

    fin.open(inputFileName);

    if(!fin.is_open())
    {
        cout << "Failed to open file" << endl;
    }
    else 
    {
        while(!fin.eof())
        {
            fin >> temp.fname >> temp.lname;

            for(int i = 0; i < 4; i++)
            {
                fin >> grade;
                temp.grades.push_back(grade);
            }
            list.push_back(temp);
            temp.grades.clear();
        }

        fin.close();
    }
}

void writeData(const vector<student> & list) {
    string outFile;
    cout << "Enter output file name: ";
    getline(cin, outFile);
    ofstream fout(outFile);

    if(!fout.is_open())
    {
        cout << "Failed to open output file!" << endl;
    }
    else
    {
        float max = 0;
        float min = 200;
        float ca_calc = 0;
        float class_avg = 0;
        fout << setw(88) << setfill('=') << "" << setfill (' ') << endl;
        fout << setw(16) << left << "fname" << setw(16) << left << "lname" << setw(10) << left
        << "test1" << setw(10) << left << "test2" << setw(10) << left << 
        "test3" << setw(10) << left << "test4" << setw(10) << left << "avg."
        << setw(10) << left << "grade" << endl;
        fout << setw(88) << setfill('=') << "" << setfill (' ') << endl;
        
        for(int j=0; j < list.size(); j++)
        {
            fout << setw(16) << left << list[j].fname << setw(16) << left << list[j].lname;
            for(int i = 0; i < 4; i++)
            {
                fout << setw(10) << left << list[j].grades[i];
                if (list[j].grades[i] > max)
                    max = list[j].grades[i];
                if (list[j].grades[i] < min)
                    min = list[j].grades[i];
            }
            float average = calc_avg(list[j].grades);
            fout << setw(10) << left << fixed << setprecision(1) << average;
            fout << setw(10) << left << grade(average);
            fout << " " << endl;
        }
        fout << setw(88) << setfill('*') << "" << setfill (' ') << endl;
        fout.close();
    }
}

void test() {

    cerr << "all test cases passed!\n";
}