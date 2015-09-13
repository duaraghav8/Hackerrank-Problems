#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef unsigned short int USHORT;

void nextMove (const int& dimension, const int& row, const int& column, const vector< string >& Grid) {
  int bot [2] = {row, column};
  int princess [2] = {0};
  string::iterator searcher;
  string temp;
  for (int i = 0; i < Grid.size (); i++) {
    temp = Grid [i];
    searcher = find (temp.begin (), temp.end (), 'p');
    if (searcher != (temp.end ())) {
      int position = distance (temp.begin (), searcher);
      princess [0] = i;
      princess [1] = position;
      break;
    }
  }
  if (bot [0] > princess [0]) {
    cout << "UP\n";
  }
  else if (bot [0] < princess [0]) {
    cout << "DOWN\n";
  }
  else if (bot [1] > princess [1]) {
    cout << "LEFT\n";
  }
  else {
    cout << "RIGHT\n";
  }
}
int main (int argc, char* argv []) {
  int gridDimension (0);
  vector< string > Grid;
  string temp;
  int botRow (0), botColumn (0);
  
  cin >> gridDimension;
  cin >> botRow;
  cin >> botColumn;
  for (int i = 0; i < gridDimension; i++) {
    cin >> temp;
    Grid.push_back (temp);
  }
  nextMove (gridDimension, botRow, botColumn, Grid);
  
  return (0);
}
