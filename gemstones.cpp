//Score: 30.0 All Correct
#include <iostream>
#include <vector>
#include <string>

using namespace std;
typedef unsigned short int USHORT;

void refineString (string& stoneList) {
  string replica;
  size_t searcher (0);
  
  replica += (stoneList [0]);
  for (int i = 1; i < stoneList.length (); i++) {
    searcher = replica.find (stoneList [i]);
    if (searcher == string::npos) {
      replica += stoneList [i];
    }
  }
  stoneList = replica;
}
int searchForGem (vector< string >& Rocks) {
  int uniqueRocks (0);
  size_t searcher (0);
  bool condition (true);
  
  for (int i = 0; i < Rocks [0].length (); i++) {
    for (int j = 1; j < Rocks.size (); j++) {
      searcher = Rocks [j].find (Rocks [0] [i]);
      if (searcher == string::npos) {
	condition = false;
	break;
      }
      else { condition = true; }
    }
    if (condition == true) { ++uniqueRocks; }
  }
  
  return (uniqueRocks);
}

int main (int argc, char* argv []) {
  int testCases (0), result (0);
  
  cin >> testCases;
  vector< string > Rocks (testCases);
  
  cin >> Rocks [0];
  refineString (Rocks [0]);
  
  for (int i = 1; i < testCases; i++) {
    cin >> Rocks [i];
  }
  result = searchForGem (Rocks);
  cout << result;
  
  return (0);
}
