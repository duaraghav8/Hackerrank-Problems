class Case:
	def __init__ (self):
		self.graph = {};
		for i in range (1, 100):
#			self.graph [str (i)] = set ([str (i + 1)]);
			self.graph [i] = set ([i + 1]);

		self.ladderNum = int (raw_input ());
		self.ladders = [];

		for i in range (0, self.ladderNum):
			ladder = [int (i) for i in raw_input ().split ()];
			self.ladders.append (ladder);
#			ladder = raw_input ().split ();
			self.graph [ladder [0]].add (ladder [1]);

		self.snakeNum = int (raw_input ());
		for i in range (0, self.snakeNum):
			snake = [int (i) for i in raw_input ().split ()];
#			snake = raw_input ().split ();
			self.graph [snake [0]].add (snake [1]);

	def getLeastRolls (self):
		rolls = 0;
		paths = list(dfs_paths(self.graph, 1, 100))
		lengths = [len (i) for i in paths];
		shortest = [int (i) for i in paths [lengths.index (min (lengths))]];
		lengthLeft = 6;

		for i in range (1, len (shortest)):
			if (self.ladders.count ([shortest [i-1], shortest [i]]) == 0):
				if (shortest [i] - shortest [i-1] <= lengthLeft):
					lengthLeft -= shortest [i] - shortest [i-1];
					if (lengthLeft == 0 or shortest [i] == 100):
						lengthLeft = 6;
						rolls += 1;
			else:
				rolls += 1;
				lengthLeft = 6;
					
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
