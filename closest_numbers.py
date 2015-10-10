size = int (input ());
array = sorted ([int (i) for i in input ().split ()]);
minGaps = [ (float ('inf'), (-1, -1)) ];
result = '';

for i in range (size - 1):
	gap = abs (array [i] - array [i + 1]);
	if (gap < minGaps [0] [0]):
		minGaps = [0];
		minGaps [0] = (gap, (array [i], array [i + 1]));
	elif (gap == minGaps [0] [0]):
		minGaps.append ( (gap, (array [i], array [i + 1])) );

for pair in minGaps:
	result += str (pair [1] [0]) + ' ' + str (pair [1] [1]) + ' ';
print (result);
