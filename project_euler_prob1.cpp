//Score: 60.0, TLE for 2 Test Cases
#include <bits/stdc++.h>
using namespace std;

long long get_count (long long number) {
	long long total (0);
	for (int i = 3; i < number; i++) {
		if (i % 3 == 0 || i % 5 == 0) {
			total += i;
		}
	}
	return (total);
}

int main () {
	int t;
	cin >> t;
	vector< long long > cases (t);

	for (int i = 0; i < t; i++) {
		cin >> cases [i];
	}
	for (int i = 0; i < t; i++) {
		cout << get_count (cases [i]) << endl;
	}
	return (0);
}
