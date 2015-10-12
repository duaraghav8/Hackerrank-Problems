def is_palindrome (string):
	return (string == string [::-1]);

t = int (input ());
strings = [input () for i in range (t)];

for string in strings:
	faulty = False;
	for i in range (len (string) // 2):
		if (not string [i] == string [len (string) - 1 - i]):
			if (is_palindrome (string [ : i] + string [i + 1 : ])):
				print (i);
			else:
				print (len (string) - 1 - i);

			faulty = True;
			break;
	if (not faulty):
		print ('-1');
