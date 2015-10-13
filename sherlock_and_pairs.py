t = int (input ());
cases = [];

for i in range (t):
	size = int (input ());
	d = {};

	vals = [int (i) for i in input ().split ()];
	for value in vals:
		try:
			d [value] += 1;
		except Exception as e:
			d [value] = 1;
	cases.append ( (size, d) );

for case in cases:
	total = 0;
	for num in case [1]:
		total += case [1] [num] * (case [1] [num] - 1) if case [1] [num] >= 2 else 0;
	print (total);
