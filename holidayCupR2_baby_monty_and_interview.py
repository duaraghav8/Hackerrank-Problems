def has_key (dic, key):
	found = False;
	try:
		found = dic [key];
	except Exception as e:
		found = False;
	return (found);

def bfs_color (graph, origin):
	RED, BLACK = 1, 0;
	queue, path = [(origin, 'r')], [];
	queue_buf, path_buf = {origin : True}, {};

	while (queue):
		path.append (queue.pop (0));
		path_buf [path [-1] [0]] = True;

		for next_node in graph [path [-1] [0]]:
			if (not (has_key (queue_buf, next_node) and has_key (path_buf, next_node))):
				queue.append ((next_node, 'b' if path [-1] [1] == 'r' else 'r'));
				queue_buf [next_node] = True;

				if (path [-1] [1] == 'r'): BLACK += 1;
				else: RED += 1;

	return ( (RED, BLACK) );

def solve (graph):
	red_count, black_count = bfs_color (graph, list (graph) [0]);
	red_count = (red_count * (red_count - 1)) // 2;
	black_count = (black_count * (black_count - 1)) // 2;
	return (red_count + black_count);

tc = int (input ());
cases = [];

for i in range (tc):
	n = int (input ());
	graph = {k : [] for k in range (1, n + 1)};

	for j in range (n - 1):
		edge = [int (k) for k in input ().split ()];
		graph [edge [0]].append (edge [1]);
		graph [edge [1]].append (edge [0]);

	cases.append (graph);

for graph in cases:
	print (solve (graph));
