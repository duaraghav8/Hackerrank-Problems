size, bottom = int (input ()), int (input ()) - 1;
array = sorted ([int (input ()) for i in range (size)]);
min_diff, top = float ('inf'), 0

while (bottom < size):
	diff = abs (array [top] - array [bottom]);
	min_diff = diff if diff < min_diff else min_diff;
	top += 1;
	bottom += 1;
print (min_diff);
