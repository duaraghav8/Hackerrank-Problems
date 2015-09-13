def sideSum (array, pos, side):
	total = 0;
	if (side == 'l'):
		if (pos == 0):
			return (total);
		for i in range (0, pos):
			total += array [i];

	else:
		if (pos == len (array) - 1):
			return (total);
		for i in range (pos + 1, len (array)):
			total += array [i];

	return (total);

def pivotExists (array):
	for i in range (0, len (array)):
		if (sideSum (array, i, 'l') == sideSum (array, i, 'r')):
			return (True);
	return (False);

n = int (input ());
cases = [];

for i in range (0, n):
	arrLen = input ();
	array = [int (i) for i in input ().split ()];
	cases.append (array);

for case in cases:
	print ('YES' if pivotExists (case) else 'NO');
