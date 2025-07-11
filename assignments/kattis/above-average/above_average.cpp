#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
    vector<int> grades;
    vector<double> percentages;

    int C;

    cin >> C;

    for (int D = 1; D <= C; D++) 
    {
        int i;
        double N;

        double sum = 0;
        double average = 0;

        double total = 0;
        double percentage;

        cin >> N;

        // Prompting the user to enter grades, and pushing them to a vector.
        for (i = 1; i <= N; i++)
        {
            int G;
            
            cin >> G;
            grades.push_back(G);
        }

        // Calculating the sum of the grades in the data set.
        for (i = 0; i <= (N-1); i++)
        {
            sum += grades[i];
        }

        average = (sum/N);

        // Calulating how much of the grades are above average.
        for (i = 0; i < N; i++) 
        {
            if(grades[i] > average) 
            {
                total += 1;
            }
        }
    
        percentage = ((total/N)*100);

        percentages.push_back(percentage);
        grades.clear();
    }

    for (int i = 0; i < percentages.size(); i++)
    {
        cout << fixed;
        cout << setprecision(3) << percentages[i] << "%" << endl;
    }
}