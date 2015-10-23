def max_rev (size, array):
	peak, cost, profit, stock = array [-1], 0, 0, 0;
	for i in range (size - 2, -2, -1):
		if (array [i] <= peak and i >= 0):
			cost += array [i];
			stock += 1;
		else:
			profit += (stock * peak) - cost;
			peak, cost, stock = array [i], 0, 0;
	return (profit);

t = int (input ());
cases = [ [int (input ()), [int (i) for i in input ().split ()]] for j in range (t) ];

for case in cases:
	print (max_rev (case [0], case [1]));
