def dijkstra (graph, start):
	spt_set, dists = set (), { node : 0 if node == start else float ('inf') for node in list (graph) };

	while (not spt_set == set (list (graph))):
		nearest = (None, float ('inf'));
		for node in dists:
			if (nearest [1] > dists [node] and spt_set.isdisjoint ([node])):
				nearest = (node, dists [node]);
		spt_set.add (nearest [0]);

		try:
			neighbours = graph [nearest [0]];
		except Exception as e:
			for node in dists: dists [node] = -1 if dists [node] == float ('inf') else dists [node];
			return (dists);

		for node in graph [nearest [0]]:
			if (dists [node [0]] > (nearest [1] + node [1])):
				dists [node [0]] = nearest [1] + node [1];
	return (dists);

t = int (input ());
cases = [];

for i in range (t):
	nodes, edges = [int (i) for i in input ().split ()];
	graph = {x : set ([]) for x in range (1, nodes + 1)};

	for j in range (edges):
		f, t, w = [int (i) for i in input ().split ()];
		graph [f].add ( (t, w) );
		graph [t].add ( (f, w) );

	start = int (input ());
	cases.append ( (nodes, edges, graph, start) );

for case in cases:
	lens = dijkstra (case [2], case [3]);
	result = [str (lens [i]) for i in lens if not i == case [3]];
	print (' '.join (result));
