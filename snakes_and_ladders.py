class Case:
	def __init__ (self):
		self.graph = {};
		for i in range (1, 100):
			self.graph [i] = set ([i + 1]);

		self.ladderNum = int (raw_input ());
		self.ladders = [];

		for i in range (0, self.ladderNum):
			ladder = [int (i) for i in raw_input ().split ()];
			self.ladders.append (ladder);
			self.graph [ladder [0]].add (ladder [1]);

		self.snakeNum = int (raw_input ());
		self.snakes = [];

		for i in range (0, self.snakeNum):
			snake = [int (i) for i in raw_input ().split ()];
			self.snakes.append (snake);
			self.graph [snake [0]].add (snake [1]);

	def getLeastRolls (self):
		rolls = 0;
		paths = list(dfs_paths(self.graph, 1, 100))
		lengths = [len (i) for i in paths];
		shortest = [int (i) for i in paths [lengths.index (min (lengths))]];
		lengthLeft = 6;
		ladderStartPoints = [ladder [0] for ladder in self.ladders];
		snakeStartPoints = [snake [0] for snake in self.snakes];

		for i in range (1, len (shortest)):
			#have to account for a snake existing en route
			if (not i == len (shortest) - 1 and snakeStartPoints.count (shortest [i+1]) > 0 and lengthLeft == 2):
				rolls += 1;
				lengthLeft = 6;
				print ("snake ", rolls, shortest [i]);
				continue;

			if ( (self.ladders.count ([shortest [i-1], shortest [i]]) == 0) and (self.snakes.count ([shortest [i-1], shortest [i]]) == 0) ):
				if (shortest [i] - shortest [i-1] <= lengthLeft):
					lengthLeft -= shortest [i] - shortest [i-1];
					if (lengthLeft == 0 or shortest [i] == 100):
						lengthLeft = 6;
						if (ladderStartPoints.count (shortest [i]) == 0):
							rolls += 1;
			else:
				rolls += 1;
				lengthLeft = 6;

			print (rolls, shortest [i]);

#		print (paths);
		print (lengths);
		print (shortest);
		return (rolls);
			

def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))

if (__name__ == '__main__'):
	t = int (raw_input ());
	cases = [];

	for i in range (0, t):
		case = Case ();
		cases.append (case);

	for case in cases:
		print (case.getLeastRolls ());
