def cavity (grid, dim):
	replica = [row.copy () for row in grid];
	for i in range (1, dim - 1):
		for j in range (1, dim - 1):
			if (grid [i] [j] > grid [i - 1] [j] and grid [i] [j] > grid [i + 1] [j] and grid [i] [j] > grid [i] [j - 1] and grid [i] [j] > grid [i] [j + 1]):
				replica [i] [j] = 'X';

	for row in replica:
		print (''.join ([str (i) for i in row]));

dim = int (input ());
grid = [];

for i in range (dim):
	grid.append ([int (i) for i in input ().strip ()]);
cavity (grid, dim);
