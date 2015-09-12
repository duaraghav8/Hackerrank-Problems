//Score: 13.9
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
enum COORDINATE {X, Y};

void displayPathToPrincess (int& m, vector< string >& grid) {
  int myBot [2], princess [2];
  string::iterator searcher;
  vector< string > moves;
  int position (0);
  
  for (int i = 0; i < m; i++) {
    if (i == 0 || i == (m-1)) {
      searcher = find ((grid [i]).begin (), (grid [i]).end (), 'p');
      if (searcher != ((grid [i]).end ())) {
	position = distance ((grid [i]).begin (), searcher);
	princess [X] = position;
	princess [Y] = i;
      }
    }
    else {
      searcher = find ((grid [i]).begin (), (grid [i]).end (), 'm');
      if (searcher != (grid [i]).end ()) {
	position = distance ((grid [i]).begin (), searcher);
	myBot [X] = position;
	myBot [Y] = i;
      }
    }
  }
  int temp = myBot [X];
  while (temp != princess [X]) {
   if (temp > princess [X]) {
      temp--;
      moves.push_back ("LEFT");
    }
    else {
      temp++;
      moves.push_back ("RIGHT");
    }
  }
  temp = myBot [Y];
  while (temp != princess [Y]) {
    if (temp < princess [Y]) {
      temp++;
      moves.push_back ("DOWN");
    }
    else {
      temp--;
      moves.push_back ("UP");
    }
  }
  for (int i = 0; i < moves.size (); i++) {
    cout << moves [i] << "\n";
  }
    
}
int main (int argc, char* argv []) {
  int dimension (0), dimCopy (0);
  string configuration;
  vector< string > Grid;
  
  cin >> dimension;
  dimCopy = dimension;
  
  while (dimension > 0) {
    cin >> configuration;
    Grid.push_back (configuration);
    
    dimension--;
  }
  
  displayPathToPrincess (dimCopy, Grid);
  return (0);
}
