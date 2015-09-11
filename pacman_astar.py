#!/usr/bin/env python3
#When the next path is built, it takes the same step that was taken last time, resulting in the same thing.
#Pacman may go back to where it came from. Prevent that

class PQueue:
	def __init__ (self):
		self.pQueue = [];

	def enqueue (self, stateInfo):
		insertPos = -1;
		for i in range (0, len (self.pQueue)):
			if (stateInfo [1] < self.pQueue [i] [1]):
				insertPos = i;
				break;

		if (insertPos == -1):
			self.pQueue.append (stateInfo);
		else:
			self.pQueue.insert (insertPos, stateInfo);
		print ('queue status: ', self.pQueue);

	def dequeue (self):
		if (len (self.pQueue) == 0):
			return (None);
		bestState = self.pQueue [0];
		self.pQueue = self.pQueue [1 : ];
		print ('queue status: ', self.pQueue);
		return (bestState [0]);

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
		stateHolder = PQueue ();
		currentState = prevState = self.pacman;

		while (True):
			nextStates = [state for state in self.getNextStates (currentState) if not state == prevState];
			print ('next states ', nextStates);
			for state in nextStates:
				heuristicCost = manhattan (self.pacman, state) + manhattan (state, self.food);
				stateHolder.enqueue ( (state, heuristicCost) );
#				print (heuristicCost);

			prevState = currentState;
			currentState = stateHolder.dequeue ();
			print ('current state: ', currentState);
			if (currentState == self.food):
				break;						

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
