def winner (a, b):
	if (a == 0 or b == 0): return ('First');
	if ( abs (a - b) % 2 == 0): return ('Second');
	return ('First');

t = int (input ());
cases = [ [int (i) for i in input ().split ()] for j in range (t) ];

for case in cases:
	print (winner (case [0], case [1]));
