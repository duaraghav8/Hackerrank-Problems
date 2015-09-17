#include <iostream>
#include <vector>

using namespace std;
typedef unsigned short int USHORT;

class Tree {
private:
  int treeHeight;
  int cycles;
  
  void updateHeight (void) {
    for (int i = 1; i <= cycles; i++) {
      if (i % 2 != 0) {
	treeHeight *= 2;
      }
      else {
	treeHeight++;
      }
    }
  }
public:
  
  Tree () : treeHeight (1) { }
  ~Tree () { }
  
  void setCycles (int parameter) {
    cycles = parameter;
    this->updateHeight ();
  } 
  int getHeight (void) const { return (treeHeight); }
};

int main (int argc, char* argv []) {
  int cycles (0);
  int testCases (0);
  
  cin >> testCases;
  vector< Tree > utopian (testCases);
  
  for (int i = 0; i < testCases; i++) {
    cin >> cycles;
    utopian [i].setCycles (cycles);
  }
  for (int i = 0; i < testCases; i++) {
    cout << (utopian [i].getHeight ()) << endl;
  }
  
  return (0);
}
