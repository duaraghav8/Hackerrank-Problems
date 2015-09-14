#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
class Case {
	private:
		int money, cost, quantity;
	public:
		Case () = default;

		void set (int m, int c, int q) {
			money = m;
			cost = c;
			quantity = q;
		}
		int getResult (void) {
			int result (0), wrappers (0);
			while (money != 0) {
				money -= cost;
				result++;
				wrappers++;

				if (wrappers == quantity) {
					result++;
					wrappers = 1;
				}
			}

			return (result);
		}
};

int main (int argc, char *argv []) {
	int testCases (0);
	int money, cost, quantity;

	cin >> testCases;
	vector< Case > cases (testCases);

	for (int i = 0; i < testCases; i++) {
		cin >> money;
		cin >> cost;
		cin >> quantity;

		cases [i].set (money, cost, quantity);
	}

	for (int i = 0; i < testCases; i++) {
		cout << cases [i].getResult () << endl;
	}

	return (0);
}
