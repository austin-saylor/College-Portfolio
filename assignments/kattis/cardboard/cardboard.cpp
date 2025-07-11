#include <iostream>

using namespace std;

int L;
int W;
int H;

int V;

int main() {
    
    cin >> V;
    
    int A;
    int cost = 6*V;
    for (L = 1; L <= V; L++)
        for (W = 1; W <= V/L; W++)
        {
            if (V%(L*W) == 0)
                {
                    H = V/(L*W);

                    A = (2*(L*W))+(2*(L*H))+(2*(H*W));
                    if (A < cost) {
                        cost = A;
                    }
                }
        }
    cout << cost << endl;
}