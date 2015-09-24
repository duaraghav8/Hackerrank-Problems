from heapq import heapify, heappush, heappop;

class Graph (object):
	def __init__ (self):
		self.numOfNodes, self.numOfEdges = [int (i) for i in input ().split ()];
		self.graph = {};

		for i in range (1, self.numOfNodes + 1):
			self.graph [i] = [];

		for i in range (self.numOfEdges):
			edge = [int (i) for i in input ().split ()];
			self.graph [edge [0]].append ( (edge [1], edge [2]) );
			self.graph [edge [1]].append ( (edge [0], edge [2]) );
		self.source = int (input ());

	def getSPCosts (self):
		costs = [str (dijkstra (self.graph, self.source, i) [0]) for i in range (1, self.numOfNodes + 1) if not i == self.source];
		return (costs);

def dijkstra (graph, start, target):
	queue = [];
	heapify (queue);
	current_node = (0, start, [start]);

	heappush (queue, current_node);
	while (not current_node [1] == target):
		try:
			current_node = heappop (queue);
		except Exception as e:
			return (-1, []);

		for neighbour in graph [current_node [1]]:
			heappush (queue, (current_node [0] + neighbour [1], neighbour [0], current_node [2] + [neighbour [0]]));

	return (current_node [0], current_node [2]);
	
if (__name__) == '__main__':
	t = int (input ());
	cases = [];

	for i in range (t):
		cases.append (Graph ());

	for case in cases:
		print (' '.join (case.getSPCosts ()));
