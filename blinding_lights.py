class Graph (object):
	def __init__ (self):
		self.numOfNodes, self.numOfEdges = [int (i) for i in input ().split ()];
		self.graph = [ [float ('inf') for j in range (0, self.numOfNodes)] for i in range (0, self.numOfNodes) ];
		self.distances = None;

		for i in range (0, self.numOfNodes):
			self.graph [i] [i] = 0;

		for i in range (0, self.numOfEdges):
			edge = [int (i) for i in input ().split ()];
			self.graph [edge [0] - 1] [edge [1] - 1] = edge [2];

	def shortest_path (self, start, target):
		if (not self.distances):
			self.distances = self.graph;
			self.distances = floyd_warshall (self.distances);

		return (self.distances [start - 1] [target - 1]);

def floyd_warshall (graph):
	nodes = len (graph);
	for k in range (0, nodes):
		for j in range (0, nodes):
			for i in range (0, nodes):
				if (graph [i] [k] + graph [k] [j] < graph [i] [j]):
					graph [i] [j] = graph [i] [k] + graph [k] [j];
	return (graph);

if (__name__) == '__main__':
	graph = Graph ();
	n = int (input ());
	queries = [];

	for i in range (0, n):
		queries.append ([int (i) for i in input ().split ()]);

	for query in queries:
		dist = graph.shortest_path (query [0], query [1]);
		print ('-1' if dist == float ('inf') else dist);
