length = input ();
array = [int (i) for i in input ().split ()];
while (array):
	print (len (array));
	minVal = min (array);
	array = [i - minVal for i in array];
	while 0 in array: array.remove (0);
