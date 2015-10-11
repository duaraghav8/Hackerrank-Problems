t = int (input ());
cases = [ (int (input()), [int (i) for i in input ().split ()]) for i in range (t) ];

for case in cases:
	total = 0;
	for i in set (case [1]):
		n = case [1].count (i);
		total += (n * (n - 1)) if n >= 2 else 0;
	print (total);
