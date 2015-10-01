t = int (input ());
strings = [];

for i in range (t):
	strings.append (list (input ()));
for string in strings:
	strLen = len (string);
	left = operations = 0;
	right = strLen - 1;

	while (right >= strLen // 2):
		while (not string [right] == string [left]):
			if (string [left] > string [right]):
				string [left] = chr (ord (string [left]) - 1);
			else:
				string [right] = chr (ord (string [right]) - 1);
			operations += 1;

		right -= 1;
		left += 1;
	print (operations);
