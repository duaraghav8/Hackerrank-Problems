def floyd_warshall (graph):
	nodes = len (graph);
	for k in range (0, nodes):
		for j in range (0, nodes):
			for i in range (0, nodes):
				if (graph [i] [k] + graph [k] [j] < graph [i] [j]):
					graph [i] [j] = graph [i] [k] + graph [k] [j];
	return (graph);
if (__name__) == '__main__':
	numOfNodes, numOfEdges = [int (i) for i in input ().split ()];
	graph = [];
	queries = [];
	for i in range (numOfNodes):
		row = [];
		for j in range (numOfNodes):
			if (i == j):
				row.append (0);
			else:
				row.append (float ('inf'));
		graph.append (row);
	for i in range (0, numOfEdges):
		edge = [int (i) for i in input ().split ()];
		graph [edge [0] - 1] [edge [1] - 1] = edge [2];

	numOfQueries = int (input ());
	for i in range (numOfQueries):
		queries.append ([int (i) for i in input ().split ()]);
	distances = floyd_warshall (graph);
	for query in queries:
		dist = distances [query [0] - 1] [query [1] - 1];
		print ('-1' if dist == float ('inf') else dist);
