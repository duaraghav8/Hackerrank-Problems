##########################MAIN LOGIC BEGINS##########################
def sp_len (n_count, e_count, graph, source):
	lengths = {i + 1 : -1 for i in range (n_count)};
	queue, visited = [(source, 0)], [];

	while (queue):
		c_node, c_dist = queue.pop (0);
		lengths [c_node] = c_dist;
		visited.append (c_node);

		for neighbour in graph [c_node]:
			if (not ( (neighbour in visited) or (neighbour in [i [0] for i in queue]) )):
				queue.append ((neighbour, c_dist + 1));

	return (lengths);
	
##########################MAIN LOGIC ENDS##########################

tc = int (input ());
graphs = [];

for i in range (tc):
	n_count, e_count = [int (i) for i in input ().split ()];
	graph = {i + 1 : [] for i in range (n_count)};

	for j in range (e_count):
		src, dest = [int (i) for i in input ().split ()]
		graph [src].append (dest);
		graph [dest].append (src);
	source = int (input ());

	graphs.append ( (n_count, e_count, graph, source) );

for pack in graphs:
	lengths = sp_len (pack [0], pack [1], pack [2], pack [3]);
	result = '';

	for i in range (pack [0]):
		if (not (i + 1 == pack [3])):
			f_len = lengths [i + 1];
			f_len *= 1 if f_len == -1 else 6;
			result += str (f_len) + ' ';

	print (result);
