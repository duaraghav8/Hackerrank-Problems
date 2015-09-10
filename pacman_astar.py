#!/usr/bin/env python3

class Path:
	def __init__ (self, pacman):
		self.path = [];
		self.path.append (pacman);

	def __lt__ (self, other):
		return (self.getCostSoFar () < other.getCostSoFar ());

	def addNewStep (self, step):
		self.path.append (step);

	def getPathSoFar (self):
		return (self.path);

	def getCostSoFar (self):
		return (len (self.path) - 1);

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

	def getNextStates (self, currentState):
		nextStates = [];

		RIGHT = [currentState [0] + 1, currentState [1]];
		LEFT = [currentState [0] - 1, currentState [1]];
		UP = [currentState [0], currentState [1] + 1];
		DOWN = [currentState [0], currentState [1] - 1];

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
		paths = [];
		pathToExpand = None;
		index = None;
		nextStates = None;
		costs = None;
		minForecastCost = None;
		minFCIndex = None;

		for i in range (0, 4):
			path = Path (self.pacman);
			paths.append (path);

		counter = 0;
		while (True):
			pathToExpand = min (paths);	#TO BE DEFINED BY OPERATOR OVERLOADING IN PATH CLASS
			print (pathToExpand.getCostSoFar (), pathToExpand.getPathSoFar ());
#			return (0);
			index = paths.index (pathToExpand);
			print (index);
			nextStates = self.getNextStates (pathToExpand.getPathSoFar () [-1]);
			print (nextStates);
#			return (0);
			costs = [pathToExpand.getCostSoFar () for i in range (0, len (nextStates))];
			costs = [];

			for i in range (0, len (nextStates)):
				costs.append (pathToExpand.getCostSoFar () + 1 + manhattan (nextStates [i], self.food));

			print (costs);
#			return (0);
			minForecastCost = min (costs);
			minFCIndex = costs.index (minForecastCost);
			print (minFCIndex);
			paths [index].addNewStep (nextStates [minFCIndex]);
			print (paths [index].getPathSoFar (), paths [index].getCostSoFar ());

			counter += 1;
			if (counter == 2):
				break;
			if (nextStates [minFCIndex] == self.food):
				return (paths [index]);

						

def manhattan (expanded_node, goal):
	distance = abs (expanded_node [0] - goal [0]) + abs (expanded_node [1] - goal [1]);
	return (distance);

def main ():
	pacman = [int (i) for i in input ().split ()];
	food = [int (i) for i in input ().split ()];
	rows_cols = [int (i) for i in input ().split ()];

	grid = Grid (pacman, food, rows_cols);
	grid.buildGrid ();

	path = grid.aStar ();
#	print ('Total cost: ', len (path) - 1);
#	for i in path:
#		print (i);
 
if (__name__) == '__main__':
	main ();
