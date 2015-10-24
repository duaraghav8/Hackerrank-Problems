#sorry for the (extremely) messy implementation, jumped into coding without planning DP is just so tempting

def max_fill (size, array):
	fill, sack = 0, {i : [0 for j in range (size)] for i in array};
	counter = 1;

	sack [array [0]] = [1 if i % array [0] == 0 else 0 for i in range (1, size + 1)];
	for i in range (size - 1, -1, -1):
		if (sack [array [0]] [i] == 1):
			fill = (i + 1);
			break;

	while (counter < len (array) and fill < size):
		for i in range (size):
			if ( (sack [array [counter - 1]] == 1) or (((i + 1) % array [counter]) == 0) ):
				sack [array [counter]] [i] = 1;
				fill = (i + 1) if (i + 1) > fill else fill;
			for j in range (array [counter], i + 1, array [counter]):
				if (i - j >= 0 and sack [array [counter - 1]] [i - j] == 1):
					sack [array [counter]] [i] = 1;
					fill = i + 1 if i + 1 > fill else fill;
					break;
		counter += 1;
	return (fill);

t = int (input ());
cases = [ ([int (i) for i in input ().split ()], [int (i) for i in input ().split ()]) for j in range (t) ];

for case in cases:
	print (max_fill (case [0] [1], sorted (set (case [1]))));
