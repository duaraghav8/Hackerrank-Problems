//After modeling the data graphically, you realize that there are only 2 types of outcomes (easily observable from the graph)
#include <iostream>
using namespace std;

int main()
{
    double number (0.);
    cin >> number;
    
    if (number < 4.) {
        cout << number * 2. << endl;
    }
    else {
        cout << 8.00 << endl;
    }
    
    return (0);
}
