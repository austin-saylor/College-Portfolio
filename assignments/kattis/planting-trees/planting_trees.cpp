#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {

    int N;
    int t;
    int i;

    int growth_time;

    vector<int> day_counts;
    vector<int> growth_times;

    cin >> N;

    for (i = 0; i < N; i++) {
        cin >> t;
        day_counts.push_back(t);
    }

    sort(day_counts.begin(), day_counts.end(), greater<int>());

    for (i = 0; i < day_counts.size(); i++) {
        growth_time = day_counts[i] + (i+1);
        growth_times.push_back(growth_time);
    }

    int P = *max_element(growth_times.begin(), growth_times.end()) + 1;
    cout << P << endl;
}