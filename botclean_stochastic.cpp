//Score: 10.0
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef unsigned short int USHORT;

void nextMove (const int& posx, const int& posy, const vector< string >& Grid) {
  int dirtyCell [2] = {0};
  string::iterator searcher;
  string temp;
  
  for (int i = 0; i < 5; i++) {
    temp = (Grid [i]);
    searcher = find (temp.begin (), temp.end (), 'd');
    if (searcher != temp.end ()) {
      int position = distance (temp.begin (), searcher);
      dirtyCell [0] = i;
      dirtyCell [1] = position;
      break;
    }
  }
  if (posx < dirtyCell [0]) {
    cout << "DOWN\n";
  }
  else if (posx > dirtyCell [0]) {
    cout << "UP\n";
  }
  else if (posy < dirtyCell [1]) {
    cout << "RIGHT\n";
  }
  else if (posy > dirtyCell [1]) {
    cout << "LEFT\n";
  }
  else {
    cout << "CLEAN\n";
  }
}
int main (int argc, char* argv []) {
  int myBot [2] = {0};
  vector< string > Grid;
  string temp;
  
  cin >> myBot [0] >> myBot [1];
  for (int i = 0; i < 5; i++) {
    cin >> temp;
    Grid.push_back (temp);
  }
  nextMove (myBot [0], myBot [1], Grid);
  return (0);
}
