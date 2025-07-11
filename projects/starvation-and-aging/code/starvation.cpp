#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <queue>
#include <functional>

class ThreadTask {
public:
    ThreadTask(int id, int priority) : id(id), priority(priority) {}

    int id;
    int priority;

    bool operator<(const ThreadTask& other) const {
        return priority > other.priority;
    }
};

std::mutex mtx;
std::condition_variable cv;
std::priority_queue<ThreadTask> task_queue;
int low_priority_task_count = 0;

bool finished = false;
std::chrono::time_point<std::chrono::high_resolution_clock> start_time;

void high_priority_task(int id, int priority) {
    ThreadTask task(id, priority);

    {
        std::unique_lock<std::mutex> lock(mtx);
        task_queue.push(task);
        std::cout << "High-priority task added: Thread " << id << " with priority " << priority << "\n";
    }

    cv.notify_all();

    std::unique_lock<std::mutex> lock(mtx);
    while (true) {
        cv.wait(lock, [&]() {
            return finished || (!task_queue.empty() && task_queue.top().id == id);
        });

        if (finished) break;

        if (!task_queue.empty() && task_queue.top().id == id) {
            std::cout << "High-priority task executing: Thread " << id << " is executing with priority " << priority << "\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(100));

            task_queue.pop();

            cv.notify_all();
            break;
        }
    }
}

void add_high_priority_tasks() {
    int task_id = 50;
    int index = 51;
    while (!finished) {
        std::this_thread::sleep_for(std::chrono::milliseconds(50)); // Add high-priority tasks frequently
        std::thread(high_priority_task, index, 0).detach();
        index++;
    }
}

void add_low_priority_tasks(int num_low_priority_threads) {
    for (int i = 0; i < num_low_priority_threads; ++i) {
        int priority = i + 1;
        int id = i + 1;
        ThreadTask task(id, priority);
        {
            std::unique_lock<std::mutex> lock(mtx);
            task_queue.push(task);
            std::cout << "Low-priority task added: Thread " << id << " with priority " << priority << "\n";
        }
    }
    low_priority_task_count = num_low_priority_threads;
}

void execute_tasks() {
    while (true) {
        ThreadTask task(-1, -1);
        {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&]() {
                return finished || !task_queue.empty();
            });

            if (finished && task_queue.empty()) break;

            if (!task_queue.empty()) {
                task = task_queue.top();
                task_queue.pop();
            }
        }

        if (task.id != -1) {
            std::cout << (task.priority == 0 ? "High-priority" : "\nLow-priority") 
                      << " task executing: Thread " << task.id << " is executing with priority " << task.priority << "\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(100));

            if (task.priority != 0) {
                std::unique_lock<std::mutex> lock(mtx);
                low_priority_task_count--;
                if (low_priority_task_count == 0) {
                    auto end_time = std::chrono::high_resolution_clock::now();
                    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
                    std::cout << "All low-priority tasks have been executed. Time taken: " << duration << " milliseconds.\n";
                    exit(1);
                }
            }

            cv.notify_all();
        }
    }
}

int main() {
    std::vector<std::thread> low_priority_threads;
    const int num_low_priority_threads = 50;

    // Record the start time
    start_time = std::chrono::high_resolution_clock::now();

    // Start the thread that adds high-priority tasks immediately
    std::thread high_priority_thread(add_high_priority_tasks);

    // Initialize low-priority tasks
    add_low_priority_tasks(num_low_priority_threads);

    // Start a thread to execute tasks
    std::thread task_executor(execute_tasks);

    // Let the threads run for some time
    std::this_thread::sleep_for(std::chrono::seconds(5));

    // Signal threads to finish
    {
        std::unique_lock<std::mutex> lock(mtx);
        finished = true;
    }
    cv.notify_all();

    if (task_executor.joinable()) {
        task_executor.join();
    }

    if (high_priority_thread.joinable()) {
        high_priority_thread.join();
    }

    std::cout << "All threads finished execution.\n";
    return 0;
}
