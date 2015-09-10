#!/usr/bin/env python3

class Grid:
	def __init__ (self, pacman, food, rows_cols):
		self.pacman = pacman;
		self.food = food;
		self.rows_cols = rows_cols;
		self.grid = [];

	def buildGrid (self):
		for i in range (0, self.rows_cols [0]):
			row = input ();
			self.grid.append (row);

		self.aStar ();

	def getNextStates (self):
		nextStates = [];

		RIGHT = [self.pacman [0] + 1, self.pacman [1]];
		LEFT = [self.pacman [0] - 1, self.pacman [1]];
		UP = [self.pacman [0], self.pacman [1] + 1];
		DOWN = [self.pacman [0], self.pacman [1] - 1];

		if (not self.grid [RIGHT [0]] [RIGHT [1]] == '%'):
			nextStates.append (RIGHT);
		if (not self.grid [LEFT [0]] [LEFT [1]] == '%'):
                        nextStates.append (LEFT);
		if (not self.grid [UP [0]] [UP [1]] == '%'):
                        nextStates.append (UP);
		if (not self.grid [DOWN [0]] [DOWN [1]] == '%'):
                        nextStates.append (DOWN);

		return (nextStates);

	def aStar (self):
		pass;
		
def manhattan (goal, expanded_node):
	distance = abs (expanded_node [0] - goal [0]) + abs (expanded_node [1] - goal [1]);
	return (distance);

def main ():
	pacman = [int (i) for i in input ().split ()];
	food = [int (i) for i in input ().split ()];
	rows_cols = [int (i) for i in input ().split ()];

	grid = Grid (pacman, food, rows_cols);
	grid.buildGrid ();
 
if (__name__) == '__main__':
	main ();
