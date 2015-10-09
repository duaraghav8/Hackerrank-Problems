#include <bits/stdc++.h>
using namespace std;

int main () {
	int t (0);
	cin >> t;

	vector< unsigned int > cases (t);
	for (int i = 0; i < t; i++) {
		cin >> cases [i];
	}
	for (auto i : cases) {
		cout << ~i << endl;
	}
	return (0);
}
