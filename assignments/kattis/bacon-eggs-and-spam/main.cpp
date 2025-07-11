#include <iostream>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

void test(void);

int main(int argc, char * argv[])
{
    if(argc > 1 && string(argv[1]) == "test")
    {
        test();
        return 0;
    }
    int N;
    string word;
    string name;
    string line;
    map<string,vector<string> > orders;

    cin >> N;
    while(N > 0)
    {
        cin.ignore(100, '\n');
        for(int i = 0; i < N; i++)
        {
            getline(cin, line);
            istringstream sline(line);
            sline >> name;
            while(sline >> word)
            {
                orders[word].push_back(name);
                //cout << name << " " << word << endl;
            }
        }
        for (auto order : orders) 
        {
            cout << order.first;
            sort(order.second.begin(), order.second.end());
            for (auto customer: order.second)
            {
                cout << " " << customer;
            }
            cout << endl;
        }

        orders.clear();
        cout << endl;
        cin >> N;
    }


    return 0;
}

void test()
{

}