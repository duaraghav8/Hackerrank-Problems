t =  int (input ());
cases = [];
for i in range (t):
	cases.append (list (input ()));
for case in cases:
	counter = i = 0;
	while (True):
		if (i >= len (case) - 1):
			break;
		if (case [i] == case [i + 1]):
			case.pop (i + 1);
			counter += 1;
			i -= 1;
		i += 1;
	print (counter);
