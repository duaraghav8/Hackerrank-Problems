//@rotten_eggs hope the code is clear
//Compilation:
// g++ map.cpp -std=c++11 -o map
//=================================================================================================================================
#include <bits/stdc++.h>	//Includes all the necessary files by default (iostream, string, set, map, queue, etc.)
#include <cmath>
using namespace std;

int pair_count (vector< int >& array, map< int, int >& myMap, int& diff) {
	int result (0);
	/*
	we look at myMap key-by-key.
	If key = 5 and diff = 2 (see the test case), then we know that we should either be looking for a 3 or a 7.
	So we follow a convention of only looking upward in the number line, i.e., when we encounter 5, we only look to see if 7 exists.
	Don't think we are skipping the 3. If 3 exists somewhere later in the map, 3 will be looking for 5 (which exists).
	*/
	for (auto i : array) {
		if (myMap [abs (i + diff)] == 1) { result++; }
	}

	return (result);
}

int main () {
	int size (0), diff (0);
	vector< int > array;
	map< int, int > myMap;

	cin >> size >> diff;
	for (int i = 0; i < size; i++) {
		int key (0);
		cin >> key;

		array.push_back (key);
		myMap [key] = 1;
	}

	cout << pair_count (array, myMap, diff) << endl;
}
