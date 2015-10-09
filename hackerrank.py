t = int (input ());
strings = [input () for i in range (t)];

for string in strings:
	a, b = string.startswith ('hackerrank'), string.endswith ('hackerrank');
	if (a and b):
		print (0);
	elif (a):
		print (1);
	elif (b):
		print (2);
	else:
		print (-1);

