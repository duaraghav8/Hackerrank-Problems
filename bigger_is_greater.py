def getNextLex (string):
	pos = posNext = -1;
	for i in range (len (string) - 1):
		if (string [i] < string [i + 1]):
			pos = i;
	if (pos == -1):
		return ('no answer');

	for j in range (pos + 1, len (string)):
		if (string [j] > string [pos]):
			posNext = j;

	temp = string [pos];
	string [pos] = string [posNext];
	string [posNext] = temp;

	temp = string [pos + 1 : ];
	string = string [ : pos + 1];
	temp.reverse ();

	return (''.join (string + temp));

t = int (input ());
strings = [];

for i in range (t):
	strings.append (list (input ()));
for string in strings:
	print (getNextLex (string));
