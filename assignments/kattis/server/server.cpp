#include <iostream>
#include <vector>

using namespace std;

int n;
int T;
int task_number = 0;
int total_time;

vector<int> tasks;

void checkTasks();

int main() {
    int i;
    int task;

    cin >> n >> T;

    for (i = 1; i <= n; i++) {
        cin >> task;
        tasks.push_back(task);
    }

    checkTasks();
    cout << task_number << endl;
}

void checkTasks() {
    int index;

    for(index = 0; index <= tasks.size(); index++) {
        total_time += tasks[index];
        if (total_time > T) {
            break;
        } else {
            task_number += 1;
        }

        if(task_number > n) {
            task_number = n;
        }
    }
}